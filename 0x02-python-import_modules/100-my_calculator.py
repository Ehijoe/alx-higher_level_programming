#!/usr/bin/python3
"""A simple calculator."""

import sys
from calculator_1 import add, sub, mul, div


def main():
    """Entry point."""
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, operator, b, _get_operator_func(operator)))


def _get_operator_func(operator):
    """Get the function that applies an operator."""
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }
    func = operators.get(operator)
    if func is None:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    return func


if __name__ == '__main__':
    main()
