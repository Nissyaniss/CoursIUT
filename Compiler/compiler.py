from __future__ import annotations

import parser
from parser import Node


def compile_program(program: parser.Program):
    return ""
    return f"""
def {program.name}() -> None:
    {convert_typedefs(self.types)}
    {instrjoin.join(instr.convert() for instr in self.body)}

if __name__ == "main":
    {program.name}()
""".strip()


# def indent()


def _compile(node: Node) -> str:
    if isinstance(node, parser.Program):
        return compile_program(node)
    else:
        print("TODO")
        return ""


def check_toplevel(node: Node) -> bool:
    print(node)
    if not isinstance(node, (parser.Program, parser.Function, parser.Procedure)):
        print(f"\033[31m[ERROR] Invalid top level instruction:\033[0m {type(node).__name__}")
        print("\033[34mHint\033[0m: you must put this instruction in a program, a function or a procedure")
        return False
    return True


def compile(nodes: list[Node]) -> str:
    return "\n".join(map(_compile, filter(check_toplevel, nodes)))
