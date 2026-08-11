from tools.math_tools import add, divide, multiply, square_root


def test_add():
    assert add.invoke({"a": 42, "b": 58}) == 100


def test_multiply():
    assert multiply.invoke({"a": 15, "b": 8}) == 120


def test_divide():
    assert divide.invoke({"a": 120, "b": 3}) == 40


def test_square_root():
    assert square_root.invoke({"a": 84}) == 84 ** 0.5