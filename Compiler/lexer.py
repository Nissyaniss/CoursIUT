from __future__ import annotations

from abc import ABC, abstractmethod

IGNORED_CHARACTERS = " \t\n"
ACCENTED_KEYWORD = {
    "à": "a",
    "début": "debut",
    "défaut": "defaut",
    "booléen": "booleen",
    "réel": "reel",
    "chaîne": "chaine",
    "répéter": "repeter",
    "procédure": "procedure",
}


class CodeStream:
    def __init__(self: CodeStream, source: str) -> None:
        self.source = source
        self.line = 1
        self.column = 1

    def peek(self: CodeStream) -> str:
        return self.source[0]

    def pop(self: CodeStream) -> str:
        char = self.source[0]
        self.source = self.source[1:]

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def __bool__(self: CodeStream) -> bool:
        return bool(self.source)


class Token(ABC):
    line: int
    column: int

    @classmethod
    @abstractmethod
    def parse(cls: type[Token], stream: CodeStream) -> Token:
        """Take the stack, fully parse this token and return the new token."""

    def __init__(self: Token, *, line: int = -1, column: int = -1) -> None:
        self.line = line
        self.column = column


class Identifier(Token):
    @classmethod
    def parse(cls: type[Identifier], stream: CodeStream) -> Identifier:
        line, column = stream.line, stream.column
        name = ""
        while stream and (stream.peek().isalnum() or stream.peek() == "_"):
            name += stream.pop()

        if name in ACCENTED_KEYWORD:
            name = ACCENTED_KEYWORD[name]

        return cls(name, line=line, column=column)

    def __init__(self: Identifier, name: str, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.name = name

    def __eq__(self: Identifier, other: object) -> bool:
        if isinstance(other, Identifier):
            return self.name == other.name
        return NotImplemented

    def __hash__(self: Identifier) -> int:
        return hash(self.name)

    def __repr__(self: Identifier) -> str:
        return f"Ident({self.name!r} at {self.line}:{self.column})"

    def __str__(self: Identifier) -> str:
        return self.name


class Integer(Token):
    @classmethod
    def parse(cls: type[Integer], stream: CodeStream) -> Integer | Float:
        line, column = stream.line, stream.column
        value = ""
        while stream and stream.peek() in "0123456789_":
            value += stream.pop()

        if stream and stream.peek() == ".":
            value += stream.pop()
            while stream and stream.peek() in "0123456789_":
                value += stream.pop()

            return Float(float(value), line=line, column=column)

        return cls(int(value), line=line, column=column)

    def __init__(self: Integer, value: int, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.value = value

    def __eq__(self: Integer, other: object) -> bool:
        if isinstance(other, Integer):
            return self.value == other.value
        return NotImplemented

    def __hash__(self: Integer) -> int:
        return hash(self.value)

    def __repr__(self: Integer) -> str:
        return f"Integer({self.value} at {self.line}:{self.column})"

    def __str__(self: Integer) -> str:
        return str(self.value)


class Float(Token):
    @classmethod
    def parse(cls: type[Float], _stream: CodeStream) -> Float:
        msg = "Please use Integer.parse to parse floats"
        raise NotImplementedError(msg)

    def __init__(self: Float, value: float, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.value = value

    def __eq__(self: Float, other: object) -> bool:
        if isinstance(other, Float):
            return self.value == other.value
        return NotImplemented

    def __hash__(self: Float) -> int:
        return hash(self.value)

    def __repr__(self: Float) -> str:
        return f"Float({self.value} at {self.line}:{self.column})"

    def __str__(self: Float) -> str:
        return str(self.value)


class Char(Token):
    @classmethod
    def parse(cls: type[Char], stream: CodeStream) -> Char:
        stream.pop()
        line, column = stream.line, stream.column

        if not stream:
            print(f"\033[31m[ERROR] Unterminated single quote at {stream.line}:{stream.column}\033[0m")
            return cls("", line=line, column=column)
        value = stream.pop()

        if not stream:
            print(f"\033[31m[ERROR] Unterminated single quote at {stream.line}:{stream.column}\033[0m")
            return cls(value, line=line, column=column)
        if (c := stream.pop()) != "'":
            value += c
            while stream and (c := stream.pop()) != "'":
                value += c
            print(f"\033[31m[ERROR] Unterminated quote at {stream.line}:{stream.column - 1} for `{value}`\033[0m")
            print(
                "\033[34mHint\033[0m: simple quotes (') can only used for the type for the single-character type 'car'."
                " If you want a 'chaîne', use double quotes (\")",
            )

        return cls(value, line=line, column=column)

    def __init__(self: Char, value: str, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.value = value

    def __eq__(self: Char, other: object) -> bool:
        if isinstance(other, Char):
            return self.value == other.value
        return NotImplemented

    def __hash__(self: Char) -> int:
        return hash(self.value)

    def __repr__(self: Char) -> str:
        return f"Char({self.value} at {self.line}:{self.column})"

    def __str__(self: Char) -> str:
        return self.value


class String(Token):
    @classmethod
    def parse(cls: type[String], stream: CodeStream) -> String:
        stream.pop()
        line, column = stream.line, stream.column
        value = ""
        escaped = False

        while stream and ((c := stream.pop()) != '"' or escaped):
            if escaped:
                if c == "\\":
                    value += "\\"
                elif c == '"':
                    value += '"'
                elif c == "\n":
                    pass
                else:
                    print(
                        f"\033[93m[WARNING] Invalid escape character at {stream.line}:{stream.column - 1}: {c}\033[0m",
                    )
                    print("\033[34mHint\033[0m: if you want to insert a literal backslash, use '\\\\'")
                    print("\033[34mHint\033[0m: valid escape characters are '\\', '\"' and '\\n'")
                    value += c
                escaped = False
            elif c == "\\":
                escaped = True
            else:
                value += c

        if c != '"':
            print(
                f"\033[31m[ERROR] Unterminated double quote at {stream.line}:{stream.column} (started at {line}:{column})\033[0m",
            )

        return cls(value, line=line, column=column)

    def __init__(self: String, value: str, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.value = value

    def __eq__(self: String, other: object) -> bool:
        if isinstance(other, String):
            return self.value == other.value
        return NotImplemented

    def __hash__(self: String) -> int:
        return hash(self.value)

    def __repr__(self: String) -> str:
        return f"String({self.value!r} at {self.line}:{self.column})"

    def __str__(self: String) -> str:
        return self.value


class CmpOperator(Token):
    @classmethod
    def parse(cls: type[CmpOperator], stream: CodeStream) -> CmpOperator | Assign:
        line, column = stream.line, stream.column

        operator = stream.pop()
        if stream and stream.peek() == "=":
            stream.pop()
            if operator == "=":
                print("\033[93m[WARNING] Pseudo-code uses `=` for equality check, not `==`\033[0m")
            else:
                operator += "="
        elif operator == "!":
            print("\033[93m[WARNING] `!` can't be alone\033[0m")
            print("\033[34mHint\033[0m: if you want the 'not equal to' operator, use `!=`")
        if operator == "<" and stream and stream.peek() == "-":
            stream.pop()
            return Assign(line=line, column=column)

        return cls(operator, line=line, column=column)

    def __init__(self: CmpOperator, op: str, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.op = op

    def __eq__(self: CmpOperator, other: object) -> bool:
        if isinstance(other, CmpOperator):
            return self.op == other.op
        return NotImplemented

    def __hash__(self: CmpOperator) -> int:
        return hash(self.op)

    def __repr__(self: CmpOperator) -> str:
        return f"CmpOperator({self.op} at {self.line}:{self.column})"

    def __str__(self: CmpOperator) -> str:
        return self.op


class MathOperator(Token):
    @classmethod
    def parse(cls: type[MathOperator], stream: CodeStream) -> MathOperator:
        line, column = stream.line, stream.column
        return cls(stream.pop(), line=line, column=column)

    def __init__(self: MathOperator, op: str, **kwargs: int) -> None:
        super().__init__(**kwargs)
        self.op = op

    def __eq__(self: MathOperator, other: object) -> bool:
        if isinstance(other, MathOperator):
            return self.op == other.op
        return NotImplemented

    def __hash__(self: MathOperator) -> int:
        return hash(self.op)

    def __repr__(self: MathOperator) -> str:
        return f"MathOperator({self.op} at {self.line}:{self.column})"

    def __str__(self: MathOperator) -> str:
        return self.op


class Comma(Token):
    value = ","

    @classmethod
    def parse(cls: type[Comma], _stream: CodeStream) -> Comma:
        msg = "Can't call Comme.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: Comma, other: object) -> bool:
        if isinstance(other, Comma):
            return True
        return NotImplemented

    def __hash__(self: Comma) -> int:
        return hash(self.value)

    def __repr__(self: Comma) -> str:
        return f"Comma at {self.line}:{self.column}"

    def __str__(self: Comma) -> str:
        return self.value


class Colon(Token):
    value = ":"

    @classmethod
    def parse(cls: type[Colon], _stream: CodeStream) -> Colon:
        msg = "Can't call Colon.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: Colon, other: object) -> bool:
        if isinstance(other, Colon):
            return True
        return NotImplemented

    def __hash__(self: Colon) -> int:
        return hash(self.value)

    def __repr__(self: Colon) -> str:
        return f"Colon at {self.line}:{self.column}"

    def __str__(self: Colon) -> str:
        return self.value


class Semicolon(Token):
    value = ";"

    @classmethod
    def parse(cls: type[Semicolon], _stream: CodeStream) -> Semicolon:
        msg = "Can't call Semicolon.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: Semicolon, other: object) -> bool:
        if isinstance(other, Semicolon):
            return True
        return NotImplemented

    def __hash__(self: Semicolon) -> int:
        return hash(self.value)

    def __repr__(self: Semicolon) -> str:
        return f"Semicolon at {self.line}:{self.column}"

    def __str__(self: Semicolon) -> str:
        return self.value


class LParen(Token):
    value = "("

    @classmethod
    def parse(cls: type[LParen], _stream: CodeStream) -> LParen:
        msg = "Can't call LParen.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: LParen, other: object) -> bool:
        if isinstance(other, LParen):
            return True
        return NotImplemented

    def __hash__(self: LParen) -> int:
        return hash(self.value)

    def __repr__(self: LParen) -> str:
        return f"LParen at {self.line}:{self.column}"

    def __str__(self: LParen) -> str:
        return self.value


class RParen(Token):
    value = ")"

    @classmethod
    def parse(cls: type[RParen], _stream: CodeStream) -> RParen:
        msg = "Can't call RParen.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: RParen, other: object) -> bool:
        if isinstance(other, RParen):
            return True
        return NotImplemented

    def __hash__(self: RParen) -> int:
        return hash(self.value)

    def __repr__(self: RParen) -> str:
        return f"RParen at {self.line}:{self.column}"

    def __str__(self: RParen) -> str:
        return self.value


class LBracket(Token):
    value = "["

    @classmethod
    def parse(cls: type[LBracket], _stream: CodeStream) -> LBracket:
        msg = "Can't call LBracket.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: LBracket, other: object) -> bool:
        if isinstance(other, LBracket):
            return True
        return NotImplemented

    def __hash__(self: LBracket) -> int:
        return hash(self.value)

    def __repr__(self: LBracket) -> str:
        return f"LBracket at {self.line}:{self.column}"

    def __str__(self: LBracket) -> str:
        return self.value


class RBracket(Token):
    value = "]"

    @classmethod
    def parse(cls: type[RBracket], _stream: CodeStream) -> RBracket:
        msg = "Can't call RParen.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: RBracket, other: object) -> bool:
        if isinstance(other, RBracket):
            return True
        return NotImplemented

    def __hash__(self: RBracket) -> int:
        return hash(self.value)

    def __repr__(self: RBracket) -> str:
        return f"RBracket at {self.line}:{self.column}"

    def __str__(self: RBracket) -> str:
        return self.value


class Assign(Token):
    value = "<-"

    @classmethod
    def parse(cls: type[Assign], _stream: CodeStream) -> Assign:
        msg = "Can't call Assign.parse direclty"
        raise NotImplementedError(msg)

    def __eq__(self: Assign, other: object) -> bool:
        if isinstance(other, Assign):
            return True
        return NotImplemented

    def __hash__(self: Assign) -> int:
        return hash(self.value)

    def __repr__(self: Assign) -> str:
        return f"Assign at {self.line}:{self.column}"

    def __str__(self: Assign) -> str:
        return self.value


class KEYWORDS:
    programme = Identifier("programme")
    debut = Identifier("debut")
    fin = Identifier("fin")
    avec = Identifier("avec")
    booleen = Identifier("booleen")
    entier = Identifier("entier")
    reel = Identifier("reel")
    car = Identifier("car")
    chaine = Identifier("chaine")
    vrai = Identifier("vrai")
    faux = Identifier("faux")
    saisir = Identifier("saisir")
    afficher = Identifier("afficher")
    si = Identifier("si")
    alors = Identifier("alors")
    sinon = Identifier("sinon")
    et = Identifier("et")
    ou = Identifier("ou")
    non = Identifier("non")
    selon = Identifier("selon")
    cas = Identifier("cas")
    defaut = Identifier("defaut")
    faire = Identifier("faire")
    pour = Identifier("pour")
    de = Identifier("de")
    a = Identifier("a")
    pas = Identifier("pas")
    tant = Identifier("tant")
    que = Identifier("que")
    repeter = Identifier("repeter")
    fonction = Identifier("fonction")
    retourne = Identifier("retourne")
    procedure = Identifier("procedure")

    # Those shouldn't be used but we still check for them
    finsi = Identifier("finsi")
    finfaire = Identifier("finfaire")


def _lexer(stream: CodeStream) -> list[Token]:
    tokens: list[Token] = []

    while stream:
        next_char = stream.peek()

        match next_char:
            case _ if next_char.isalpha() or next_char == "_":
                tokens.append(Identifier.parse(stream))
            case _ if next_char.isdigit():
                tokens.append(Integer.parse(stream))
            case "'":
                tokens.append(Char.parse(stream))
            case '"':
                tokens.append(String.parse(stream))
            case "=" | "<" | ">" | "!":
                tokens.append(CmpOperator.parse(stream))
            case "+" | "-" | "*" | "/" | "%" | "^":
                tokens.append(MathOperator.parse(stream))
            case ",":
                tokens.append(Comma(line=stream.line, column=stream.column))
                stream.pop()
            case ":":
                tokens.append(Colon(line=stream.line, column=stream.column))
                stream.pop()
            case ";":
                tokens.append(Semicolon(line=stream.line, column=stream.column))
                stream.pop()
            case "(":
                tokens.append(LParen(line=stream.line, column=stream.column))
                stream.pop()
            case ")":
                tokens.append(RParen(line=stream.line, column=stream.column))
                stream.pop()
            case "[":
                tokens.append(LBracket(line=stream.line, column=stream.column))
                stream.pop()
            case "]":
                tokens.append(RBracket(line=stream.line, column=stream.column))
                stream.pop()
            case "#":
                while stream.pop() != "\n":
                    pass
            case _ if next_char in IGNORED_CHARACTERS:
                stream.pop()
            case _:
                print(f"\033[31m[ERROR] Unknown token at {stream.line}:{stream.column}:\033[0m {stream.pop()}")

    return tokens


def lexer(code: str) -> list[Token]:
    stream = CodeStream(code)

    try:
        return _lexer(stream)
    except Exception:
        print(f"\033[31mError at {stream.line}:{stream.column}:\033[0m")
        raise
