from __future__ import annotations

import ast

from flake8_walrus import Plugin


def results(s):
    return {'{}:{}: {}'.format(*r) for r in Plugin(ast.parse(s)).run()}


def test_trivial():
    assert not results('')


def test_normal_assignment_ok():
    assert not results('x = 5')


def test_assignment_expression_not_ok():
    msg, = results('print(x := 5, x)')
    assert msg == '1:6: ASN001 do not use assignment expressions'
