import ast
from typing import Any
from typing import Generator
from typing import List
from typing import Tuple
from typing import Type

import importlib_metadata

MSG = 'ASN001 do not use assignment expressions'


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.assign_exprs: List[Tuple[int, int]] = []

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.assign_exprs.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.assign_exprs:
            yield line, col, MSG, type(self)
