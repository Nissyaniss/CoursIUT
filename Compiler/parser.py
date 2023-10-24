from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from typing import NewType, Sequence, TypeVar, overload

import lexer
from lexer import KEYWORDS, Token

TYPES = {
    KEYWORDS.booleen: bool,
    KEYWORDS.entier: int,
    KEYWORDS.reel: float,
    KEYWORDS.car: str,
    KEYWORDS.chaine: str,
}


class TokenStream:
    def __init__(self: TokenStream, tokens: list[Token]) -> None:
        self.tokens = tokens

    def peek(self: TokenStream, index: int = 0) -> Token:
        return self.tokens[index]

    def try_peek(self: TokenStream, index: int = 0) -> Token | None:
        try:
            return self.tokens[index]
        except IndexError:
            return None

    def pop(self: TokenStream) -> Token:
        return self.tokens.pop(0)

    def try_pop(self: TokenStream) -> Token | None:
        try:
            return self.tokens.pop(0)
        except IndexError:
            return None

    def put_back(self: TokenStream, token: Token) -> None:
        self.tokens.insert(0, token)

    def __bool__(self: TokenStream) -> bool:
        return bool(self.tokens)


class Node(ABC):
    @classmethod
    @abstractmethod
    def parse(cls: type[Node], stream: TokenStream) -> Node:
        pass


class Program(Node):
    @classmethod
    def parse(cls: type[Program], stream: TokenStream) -> Program:
        stream.pop()
        name = assert_token(stream.try_pop(), lexer.Identifier).name
        assert_token(stream.try_pop(), KEYWORDS.debut, crash=False)

        typedefs = []
        if stream.peek() == KEYWORDS.avec:
            typedefs = parse_typedefs(stream)

        body = parse_block(stream)

        if stream.try_peek() == lexer.Identifier("fin" + name):
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), lexer.Identifier(name), crash=False)

        return cls(name, typedefs, body)

    def __init__(self: Program, name: str, types: list[TypeDef], body: list[Node]) -> None:
        self.name = name
        self.types = types
        self.body = body

    def __repr__(self: Program) -> str:
        return f"Program({self.name}, ...)"


class Function(Node):
    @classmethod
    def parse(cls: type[Function], stream: TokenStream) -> Function:
        stream.pop()
        name = assert_token(stream.try_pop(), lexer.Identifier).name
        assert_token(stream.try_pop(), lexer.LParen, crash=False)

        def parse_list(stream: TokenStream) -> list[TypeDef]:
            types = []
            while stream and not isinstance(stream.peek(), lexer.RParen):
                name = assert_token(stream.try_pop(), lexer.Identifier).name
                assert_token(stream.try_pop(), lexer.Colon)
                typ = assert_token(stream.try_pop(), lexer.Identifier)
                types.append(TypeDef((name, typ, None)))
                if stream and isinstance(stream.peek(), lexer.Comma):
                    stream.pop()

            return types

        args = parse_list(stream)
        assert_token(stream.try_pop(), lexer.RParen, crash=False)
        assert_token(stream.try_pop(), KEYWORDS.retourne, crash=False)
        ret = assert_token(stream.try_pop(), lexer.Identifier)
        assert_token(stream.try_pop(), KEYWORDS.debut, crash=False)

        typedefs = []
        if stream.peek() == KEYWORDS.avec:
            typedefs = parse_typedefs(stream)

        body = parse_block(stream)

        if stream.try_peek() == lexer.Identifier("fin" + name):
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), lexer.Identifier(name), crash=False)

        return cls(name, args, ret, typedefs, body)

    def __init__(
        self: Function,
        name: str,
        args: list[TypeDef],
        ret: lexer.Identifier,
        types: list[TypeDef],
        body: list[Node],
    ) -> None:
        self.name = name
        self.args = args
        self.ret = ret
        self.types = types
        self.body = body

    def __repr__(self: Function) -> str:
        return f"Function({self.name}, ...)"


class Procedure(Node):
    @classmethod
    def parse(cls: type[Procedure], stream: TokenStream) -> Procedure:
        stream.pop()
        name = assert_token(stream.try_pop(), lexer.Identifier).name
        assert_token(stream.try_pop(), lexer.LParen, crash=False)

        def parse_list(stream: TokenStream) -> tuple[list[TypeDef], list[TypeDef]]:
            types: list[TypeDef] = []
            ref_types: list[TypeDef] = []
            t = types
            while stream and not isinstance(stream.peek(), lexer.RParen):
                name = assert_token(stream.try_pop(), lexer.Identifier).name
                assert_token(stream.try_pop(), lexer.Colon)
                typ = assert_token(stream.try_pop(), lexer.Identifier)
                t.append(TypeDef((name, typ, None)))
                if stream and isinstance(stream.peek(), lexer.Comma):
                    stream.pop()
                if stream and isinstance(stream.peek(), lexer.Semicolon):
                    stream.pop()
                    t = ref_types

            return (types, ref_types)

        (args, ref_args) = parse_list(stream)
        assert_token(stream.try_pop(), lexer.RParen, crash=False)
        assert_token(stream.try_pop(), KEYWORDS.debut, crash=False)

        typedefs = []
        if stream.peek() == KEYWORDS.avec:
            typedefs = parse_typedefs(stream)

        body = parse_block(stream)

        if stream.try_peek() == lexer.Identifier("fin" + name):
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), lexer.Identifier(name), crash=False)

        return cls(name, args, ref_args, typedefs, body)

    def __init__(
        self: Procedure,
        name: str,
        args: list[TypeDef],
        ref_args: list[TypeDef],
        types: list[TypeDef],
        body: list[Node],
    ) -> None:
        self.name = name
        self.args = args
        self.ref_args = ref_args
        self.types = types
        self.body = body

    def __repr__(self: Procedure) -> str:
        return f"Procedure({self.name}, ...)"


class Condition(Node):
    @classmethod
    def parse(cls: type[Condition], stream: TokenStream) -> Condition:
        stream.pop()
        condition = Expr.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.alors, crash=False)
        if_block = parse_block(stream)

        else_block = None
        if stream.peek() == KEYWORDS.sinon:
            stream.pop()
            else_block = parse_block(stream)

        if stream.try_peek() == KEYWORDS.finsi:
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), KEYWORDS.si, crash=False)

        return cls(condition, if_block, else_block)

    def __init__(self: Condition, condition: Expr, if_block: list[Node], else_block: list[Node] | None) -> None:
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def __repr__(self: Condition) -> str:
        return f"Condition({self.condition!r}, ..., ...)"


class Switch(Node):
    @classmethod
    def parse(cls: type[Switch], stream: TokenStream) -> Switch:
        stream.pop()
        binding = Binding.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)

        blocks = []
        while stream and stream.peek() == KEYWORDS.cas:
            stream.pop()
            value = Expr.parse(stream)
            assert_token(stream.try_pop(), lexer.Colon)
            block = parse_block(stream)
            blocks.append((value, block))

        default = None
        if stream.try_peek() == KEYWORDS.defaut:
            stream.pop()
            assert_token(stream.try_pop(), lexer.Colon)
            default = parse_block(stream)

        if stream.try_peek() == KEYWORDS.finfaire:
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)

        return cls(binding, blocks, default)

    def __init__(
        self: Switch,
        binding: Binding,
        blocks: list[tuple[Expr, list[Node]]],
        default: list[Node] | None,
    ) -> None:
        self.binding = binding
        self.blocks = blocks
        self.default = default

    def __repr__(self: Switch) -> str:
        return f"Switch({self.binding!r}, ...)"


class ForLoop(Node):
    @classmethod
    def parse(cls: type[ForLoop], stream: TokenStream) -> ForLoop:
        stream.pop()
        binding = Binding.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.de)
        start = Expr.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.a)
        end = Expr.parse(stream)
        step = None
        if stream.peek() == KEYWORDS.pas:
            stream.pop()
            step = Expr.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)
        block = parse_block(stream)

        if stream.try_peek() == KEYWORDS.finfaire:
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)

        return cls(binding, start, end, step, block)

    def __init__(self: ForLoop, binding: Binding, start: Expr, end: Expr, step: Expr | None, block: list[Node]) -> None:
        self.binding = binding
        self.start = start
        self.end = end
        self.step = step
        self.block = block

    def __repr__(self: ForLoop) -> str:
        return f"ForLoop(for {self.binding!r} from {self.start!r} to {self.end!r}{f' step {self.step}' if self.step else ''}, ...)"


class WhileLoop(Node):
    @classmethod
    def parse(cls: type[WhileLoop], stream: TokenStream) -> WhileLoop:
        stream.pop()
        assert_token(stream.try_pop(), KEYWORDS.que, crash=False)
        condition = Expr.parse(stream)
        assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)

        block = parse_block(stream)

        if stream.try_peek() == KEYWORDS.finfaire:
            stream.pop()
        else:
            assert_token(stream.try_pop(), KEYWORDS.fin)
            assert_token(stream.try_pop(), KEYWORDS.faire, crash=False)

        return cls(condition, block)

    def __init__(self: WhileLoop, condition: Expr, block: list[Node]) -> None:
        self.condition = condition
        self.block = block

    def __repr__(self: WhileLoop) -> str:
        return f"WhileLoop({self.condition}, ...)"


class Print(Node):
    @classmethod
    def parse(cls: type[Print], stream: TokenStream) -> Print:
        stream.pop()
        elements = []

        while (e := Expr.parse(stream)).nodes:
            elements.append(e)
            if isinstance(stream.try_peek(), lexer.Comma):
                stream.pop()
            else:
                break

        return cls(elements)

    def __init__(self: Print, elements: list[Expr]) -> None:
        self.elements = elements

    def __repr__(self: Print) -> str:
        return f"Print({', '.join(map(repr, self.elements))})"


class Input(Node):
    @classmethod
    def parse(cls: type[Input], stream: TokenStream) -> Input:
        stream.pop()
        bindings = []

        while isinstance(stream.try_peek(), lexer.Identifier):
            bindings.append(Binding.parse(stream))
            if isinstance(stream.try_peek(), lexer.Comma):
                stream.pop()
            else:
                break

        return cls(bindings)

    def __init__(self: Input, bindings: list[Binding]) -> None:
        self.bindings = bindings

    def __repr__(self: Input) -> str:
        return f"Input({', '.join(map(repr, self.bindings))})"


class Return(Node):
    @classmethod
    def parse(cls: type[Return], stream: TokenStream) -> Return:
        stream.pop()
        value = Expr.parse(stream)

        return cls(value)

    def __init__(self: Return, value: Expr) -> None:
        self.value = value

    def __repr__(self: Return) -> str:
        return f"Return({self.value!r})"


class Assignement(Node):
    @classmethod
    def parse(cls: type[Assignement], stream: TokenStream) -> Assignement:
        binding = Binding.parse(stream)
        assert_token(stream.try_pop(), lexer.Assign)
        value = Expr.parse(stream)

        return cls(binding, value)

    def __init__(self: Assignement, binding: Binding, value: Expr) -> None:
        self.binding = binding
        self.value = value

    def __repr__(self: Assignement) -> str:
        return f"Assignement({self.binding!r}, {self.value!r})"


class FuncCall(Node):
    @classmethod
    def parse(cls: type[FuncCall], stream: TokenStream) -> FuncCall:
        # This assert_token is here only to satisfy the typechecker
        name = assert_token(stream.pop(), lexer.Identifier).name
        stream.pop()

        def parse_expr_list(stream: TokenStream) -> list[Expr]:
            exprs = []
            while stream and not isinstance(stream.peek(), (lexer.RParen, lexer.Semicolon)):
                exprs.append(Expr.parse(stream))

                if stream and isinstance(stream.peek(), lexer.Comma):
                    stream.pop()

            return exprs

        def parse_binding_list(stream: TokenStream) -> list[lexer.Binding]:
            bindings = []
            while stream and not isinstance(stream.peek(), lexer.RParen):
                bindings.append(Binding.parse(stream))

                if stream and isinstance(stream.peek(), lexer.Comma):
                    stream.pop()

            return bindings

        arguments = parse_expr_list(stream)
        references = []
        if isinstance(stream.try_peek(), lexer.Semicolon):
            stream.pop()
            references = parse_binding_list(stream)

        assert_token(stream.try_pop(), lexer.RParen)

        return cls(name, arguments, references)

    def __init__(self: FuncCall, name: str, arguments: list[Expr], references: list[Binding]) -> None:
        self.name = name
        self.arguments = arguments
        self.references = references

    def __repr__(self: FuncCall) -> str:
        return f"FuncCall({self.name}, {', '.join(map(repr, self.arguments))}; {', '.join(map(repr, self.references))})"


class Expr(Node):
    all_tokens = (
        KEYWORDS.vrai,
        KEYWORDS.faux,
        lexer.Integer,
        lexer.Float,
        lexer.Char,
        lexer.String,
        lexer.CmpOperator,
        lexer.MathOperator,
        KEYWORDS.et,
        KEYWORDS.ou,
        KEYWORDS.non,
        lexer.Identifier,
        lexer.LParen,
    )

    @classmethod
    def parse(cls: type[Expr], stream: TokenStream) -> Expr:
        nodes: list[Node] = []

        while stream:
            next_token = stream.peek()

            if next_token == KEYWORDS.vrai:
                nodes.append(Value(True))
                stream.pop()
            elif next_token == KEYWORDS.faux:
                nodes.append(Value(False))
                stream.pop()
            elif isinstance(next_token, (lexer.Integer, lexer.Float, lexer.Char, lexer.String)):
                nodes.append(Value(next_token.value))
                stream.pop()
            elif isinstance(next_token, (lexer.CmpOperator, lexer.MathOperator)):
                nodes.append(Operator(next_token.op))
                stream.pop()
            elif next_token in (KEYWORDS.et, KEYWORDS.ou, KEYWORDS.non):
                nodes.append(Operator(next_token.name))
                stream.pop()
            elif (not nodes or isinstance(nodes[-1], Operator)) and isinstance(next_token, lexer.Identifier):
                if isinstance(stream.try_peek(1), lexer.LParen):
                    nodes.append(FuncCall.parse(stream))
                else:
                    nodes.append(Binding.parse(stream))
            elif isinstance(next_token, lexer.LParen):
                stream.pop()
                nodes.append(Expr.parse(stream))
                assert_token(stream.try_pop(), lexer.RParen)
            elif not nodes:
                assert_token(stream.try_pop(), cls.all_tokens)
            else:
                break

        return cls(nodes)

    def __init__(self: Expr, nodes: list[Node]) -> None:
        self.nodes = nodes

    def __repr__(self: Expr) -> str:
        return f"Expr({' '.join(map(repr, self.nodes))})"


class Value(Node):
    @classmethod
    def parse(cls: type[Value], _stream: TokenStream) -> Value:
        msg = "Can't call Value.parse direclty"
        raise NotImplementedError(msg)

    def __init__(self: Value, value: bool | int | float | lexer.Char | str) -> None:
        self.value = value

    def __repr__(self: Value) -> str:
        return f"Value({self.value})"


class Binding(Node):
    @classmethod
    def parse(cls: type[Binding], stream: TokenStream) -> Binding:
        binding = assert_token(stream.try_pop(), lexer.Identifier)

        index = None
        if stream and isinstance(stream.peek(), lexer.LBracket):
            stream.pop()
            index = Expr.parse(stream)
            assert_token(stream.try_pop(), lexer.RBracket)

        return cls(binding, index)

    def __init__(self: Binding, name: lexer.Identifier, index: Expr | None) -> None:
        self.name = name
        self.index = index

    def __repr__(self: Binding) -> str:
        return f"Binding({self.name}{f'[{self.index!r}]' if self.index else ''})"


class Operator(Node):
    @classmethod
    def parse(cls: type[Operator], _stream: TokenStream) -> Operator:
        msg = "Can't call Operator.parse direclty"
        raise NotImplementedError(msg)

    def __init__(self: Operator, op: str) -> None:
        self.op = op

    def __repr__(self: Operator) -> str:
        return f"Operator({self.op})"


TypeDef = NewType("TypeDef", tuple[str, lexer.Identifier, Expr | None])
T = TypeVar("T", bound=Token)


@overload
def assert_token(token: Token | None, expected: Sequence[T | type[T]], *, crash: bool = True) -> T:
    ...


@overload
def assert_token(token: Token | None, expected: type[T], *, crash: bool = True) -> T:
    ...


@overload
def assert_token(token: Token | None, expected: T, *, crash: bool = True) -> T:
    ...


def assert_token(token, expected, *, crash=True):
    if isinstance(expected, (Token, type)):
        expected = (expected,)

    expected_str = ((repr(str(x)) if isinstance(x, Token) else x.__name__) for x in expected)

    if token is None:
        print("\033[31m[ERROR] No token found.")
        print(f"\033[34mHint\033[0m: expected one of: {', '.join(expected_str)}")
        if crash:
            sys.exit()
        else:
            return None

    for x in expected:
        if isinstance(x, Token) and token == x:
            break
        if isinstance(x, type) and isinstance(token, x):
            break
    else:
        print(f"\033[31m[ERROR] Unexpected token:\033[0m `{token}` at {token.line}:{token.column}.")
        print(f"\033[34mHint\033[0m: expected one of: {', '.join(expected_str)}")
        if crash:
            sys.exit()

    return token


def parse_typedefs(stream: TokenStream) -> list[TypeDef]:
    def parse_list(stream: TokenStream) -> list[lexer.Identifier]:
        idents = []
        while isinstance(stream.peek(), lexer.Identifier):
            idents.append(stream.pop())
            if isinstance(stream.peek(), lexer.Comma):
                idents[-1].comma = stream.pop()
            else:
                break

        return idents

    def unparse_list(stream: TokenStream, idents: Sequence[lexer.Identifier]) -> None:
        for ident in idents:
            stream.put_back(ident)
            if hasattr(ident, "comma"):
                stream.put_back(ident.comma)

    stream.pop()
    types = []

    while isinstance(stream.peek(), lexer.Identifier):
        idents = parse_list(stream)
        if not isinstance(stream.peek(), lexer.Colon):
            unparse_list(stream, idents)
            break

        assert_token(stream.pop(), lexer.Colon)
        typ_ = assert_token(stream.pop(), tuple(TYPES.keys()))
        value = None
        if isinstance(stream.peek(), lexer.Assign):
            stream.pop()
            value = Expr.parse(stream)

        types += [TypeDef((ident.name, typ_, value)) for ident in idents]

    return types


def parse_block(stream: TokenStream) -> list[Node]:
    nodes: list[Node] = []

    while stream:
        next_token = stream.peek()
        assert_token(
            next_token,
            (
                KEYWORDS.programme,
                KEYWORDS.fonction,
                KEYWORDS.procedure,
                KEYWORDS.si,
                KEYWORDS.selon,
                KEYWORDS.pour,
                KEYWORDS.tant,
                KEYWORDS.saisir,
                KEYWORDS.afficher,
                KEYWORDS.fin,
                KEYWORDS.sinon,
                KEYWORDS.cas,
                KEYWORDS.defaut,
                lexer.Identifier,
            ),
            crash=False,
        )

        if next_token == KEYWORDS.programme:
            nodes.append(Program.parse(stream))
        elif next_token == KEYWORDS.fonction:
            nodes.append(Function.parse(stream))
        elif next_token == KEYWORDS.procedure:
            nodes.append(Procedure.parse(stream))
        elif next_token == KEYWORDS.si:
            nodes.append(Condition.parse(stream))
        elif next_token == KEYWORDS.selon:
            nodes.append(Switch.parse(stream))
        elif next_token == KEYWORDS.pour:
            nodes.append(ForLoop.parse(stream))
        elif next_token == KEYWORDS.tant:
            nodes.append(WhileLoop.parse(stream))
        elif next_token == KEYWORDS.saisir:
            nodes.append(Input.parse(stream))
        elif next_token == KEYWORDS.afficher:
            nodes.append(Print.parse(stream))
        elif next_token == KEYWORDS.saisir:
            nodes.append(Input.parse(stream))
        elif next_token == KEYWORDS.retourne:
            nodes.append(Return.parse(stream))
        elif next_token in (KEYWORDS.fin, KEYWORDS.sinon, KEYWORDS.cas, KEYWORDS.defaut):
            return nodes
        elif isinstance(next_token, lexer.Identifier) and next_token.name.startswith("fin"):
            print("\033[93m[WARNING] Using a space for the end of a block is preferred\033[0m")
            print(f"\033[34mHint\033[0m: use `fin {next_token.name[3:]}`")
            return nodes
        elif isinstance(next_token, lexer.Identifier) and isinstance(stream.try_peek(1), lexer.LParen):
            nodes.append(FuncCall.parse(stream))
        elif isinstance(next_token, lexer.Identifier):
            nodes.append(Assignement.parse(stream))
        else:
            stream.pop()

    return nodes


def parse(tokens: list[Token]) -> list[Node]:
    stream = TokenStream(tokens)
    return parse_block(stream)
