#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3

from __future__ import annotations

import parser
import re
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, TypeVar

import lexer
from compiler import compile
from lexer import KEYWORDS, Token

CODE_BLOCK_REGEX = re.compile(r"## (?P<name>(\w| )+)\n+```\n(?P<code>.+?)\n```", re.DOTALL)


class TokenStack:
    def __init__(self: TokenStack, tokens: list[Token]) -> None:
        self.tokens = tokens

    def peek(self: TokenStack) -> Token:
        return self.tokens[0]

    def pop(self: TokenStack) -> Token | None:
        try:
            return self.tokens.pop(0)
        except IndexError:
            return None

    def put_back(self: TokenStack, token: Token) -> None:
        self.tokens.insert(0, token)

    def __bool__(self: TokenStack) -> bool:
        return bool(self.tokens)


class Node(ABC):
    @abstractmethod
    def parse(self: Node, stack: TokenStack) -> Node:
        pass

    @abstractmethod
    def convert(self: Node, *, indentation: int) -> str:
        pass


class Program(Node):
    def parse(self: Program, stack: TokenStack) -> Program:
        # remove the 'programme'
        stack.pop()
        self.name = assert_token(stack.pop(), lexer.Identifier).name
        assert_token(stack.pop(), KEYWORDS.debut)
        self.types = parse_typedefs(stack)
        self.body = parse_block(stack)
        assert_token(stack.pop(), KEYWORDS.fin)
        assert_token(stack.pop(), lexer.Identifier(self.name))

        return self

    def convert(self: Program, *, indentation: int = 0) -> str:
        instrjoin = "\n    "
        return f"""
def {self.name}() -> None:
    {convert_typedefs(self.types)}
    {instrjoin.join(instr.convert() for instr in self.body)}

if __name__ == "main":
    {self.name}()
    """.strip()

    def __repr__(self: Program) -> str:
        return f"Program({self.name})"


class Condition(Node):
    def parse(self: Condition, stack: TokenStack) -> Condition:
        stack.pop()
        self.condition = parse_expr(stack)
        assert_token(stack.pop(), KEYWORDS.alors)
        self.if_yes = parse_block(stack)

        self.if_no = None
        if stack.peek() == KEYWORDS.sinon:
            stack.pop()
            self.if_no = parse_block(stack)

        assert_token(stack.pop(), KEYWORDS.fin)
        assert_token(stack.pop(), KEYWORDS.si)

        return self

    def convert(self: Condition, *, indentation: int = 0) -> str:
        # jointer = "\n" + " " * indentation
        # lines = [f"if {self.condition.convert()}:", self.if_yes]
        # return jointer.join(lines)
        return ""


class Input(Node):
    def parse(self: Input, stack: TokenStack) -> Input:
        stack.pop()
        self.variable = assert_token(stack.pop(), lexer.Identifier).name

        return self

    def convert(self: Input) -> str:
        return f"{self.variable} = input()"


class Print(Node):
    def parse(self: Print, stack: TokenStack) -> Print:
        stack.pop()
        self.message = [parse_expr(stack)]
        while isinstance(stack.peek(), lexer.Comma):
            stack.pop()
            self.message.append(parse_expr(stack))

        return self

    def convert(self: Print) -> str:
        def convert(value) -> str:
            if isinstance(value, lexer.String):
                return f'"{value.value}"'
            return None

        return f"""print({', '.join(map(convert, self.message))})"""


T = TypeVar("T")


def convert_typedefs(typedefs: list[tuple[str, type, Any]], *, indent=4) -> str:
    lines = []
    for name, typ, value in typedefs:
        if value is None:
            lines.append(f"{name}: {typ.__name__}")
        else:
            lines.append(f"{name}: {typ.__name__} = {value}")

    return ("\n" + " " * indent).join(lines)


def assert_token(token: Token | None, expected: tuple[type | Token] | type | Token) -> Token:
    if not isinstance(expected, tuple):
        expected = (expected,)

    if token is None:
        print(
            f"\033[31m[ERROR] No token found. Expected one of: {''.join(map(repr, expected))}",
        )
        sys.exit()

    if isinstance(expected[0], type):
        if not isinstance(token, expected):
            print(
                f"\033[31m[ERROR] Unexpected token:\033[0m {token} at line {token.line}. Expected one of: {''.join(map(repr, expected))}",
            )
            sys.exit()
    else:
        if token not in expected:
            print(
                f"\033[31m[ERROR] Unexpected token:\033[0m {token} at line {token.line}. Expected one of: {''.join(map(repr, expected))}",
            )
            sys.exit()

    return token


def parse_expr(stack: TokenStack) -> lexer.String:
    next_token = assert_token(stack.peek(), (lexer.String,))
    if isinstance(next_token, lexer.String):
        return stack.pop()
    return None


def parse_list(stack: TokenStack, token_type: type) -> list[Token]:
    tokens = []
    while isinstance(stack.peek(), token_type):
        tokens.append(stack.pop())
        if isinstance(stack.peek(), lexer.Comma):
            stack.pop()
        else:
            break

    return tokens


BOOL_VALUES = {KEYWORDS.vrai: True, KEYWORDS.faux: False}


def parse_value(stack: TokenStack, typ: lexer.Identifier) -> Any:
    if typ == KEYWORDS.booleen:
        return BOOL_VALUES[assert_token(stack.pop(), tuple(BOOL_VALUES.keys()))]
    elif typ == KEYWORDS.entier:
        return assert_token(stack.pop(), lexer.Integer).value
    elif typ == KEYWORDS.reel:
        print("TODO")
        return None
    elif typ == KEYWORDS.car:
        print("TODO")
        return None
    elif type == KEYWORDS.chaine:
        return assert_token(stack.pop(), lexer.String).value
    return None


TYPEMAP = {
    KEYWORDS.booleen: bool,
    KEYWORDS.entier: int,
    KEYWORDS.reel: float,
    KEYWORDS.car: str,
    KEYWORDS.chaine: str,
}


def parse_typedefs(stack: TokenStack) -> list[tuple[str, type, Any]]:
    assert_token(stack.pop(), KEYWORDS.avec)
    types = []

    while isinstance(stack.peek(), lexer.Identifier):
        idents = (token.name for token in parse_list(stack, lexer.Identifier))
        if not isinstance(stack.peek(), lexer.Colon):
            idents = list(idents)
            assert len(idents) == 1
            stack.put_back(lexer.Identifier(idents[0]))
            break
        assert_token(stack.pop(), lexer.Colon)
        typ = assert_token(stack.pop(), tuple(TYPEMAP.keys()))
        value = None
        if isinstance(stack.peek(), lexer.Assign):
            stack.pop()
            value = parse_value(stack, typ)

        types += [(ident, TYPEMAP[typ], value) for ident in idents]

    return types


def parse_block(stack: TokenStack) -> list[Node]:
    nodes = []

    while stack:
        next_token = stack.peek()
        # assert_token(next_token, (KeywordToken,))

        if next_token == KEYWORDS.programme:
            nodes.append(Program().parse(stack))
        elif next_token == KEYWORDS.si:
            nodes.append(Condition().parse(stack))
        elif next_token == KEYWORDS.afficher:
            nodes.append(Print().parse(stack))
        elif next_token == KEYWORDS.saisir:
            nodes.append(Input().parse(stack))
        elif next_token in (KEYWORDS.fin, KEYWORDS.alors):
            return nodes
        else:
            token = stack.pop()
            print(f"\033[31m[ERROR] Unexpected token:\033[0m {token} at line {token.line}")

    return nodes


def parse(code: TokenStack) -> list[Node]:
    return parse_block(code)


def compile2(code: str) -> str:
    tokens = lexer.lexer(code)
    # asts = parse(TokenStack(tokens))
    asts = parser.parse(tokens)

    return "\n\n".join(ast.convert() for ast in asts) + "\n"


def compilefull(code: str) -> str:
    tokens = lexer.lexer(code)
    asts = parser.parse(tokens)
    return compile(asts)


def main() -> None:
    input_file = Path(sys.argv[1])
    file = input_file.read_text()

    for name, _, code in re.findall(CODE_BLOCK_REGEX, file):
        print(f"Compiling {name}")
        Path(f"{input_file.stem} - {name}.pseudo.py").write_text(compilefull(code))


if __name__ == "__main__":
    main()
