import math

from langchain_core.tools import tool


@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


@tool
def square_root(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")

    return math.sqrt(a)


MATH_TOOLS = [
    add,
    multiply,
    divide,
    square_root,
]