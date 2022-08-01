from __future__ import annotations

import ast
from typing import Any
from typing import Generator

MSG = 'ASN001 do not use assignment expressions'


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.assign_exprs: list[tuple[int, int]] = []

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.assign_exprs.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.assign_exprs:
            yield line, col, MSG, type(self)
