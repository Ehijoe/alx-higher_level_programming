#!/usr/bin/python3
"""Text indentation."""


def text_indentation(text):
    """Print a string with newlines after some tokens.

    Accepted tokens are '.', '?' and ':'.
    Whitespace after the token is stripped.
    """
    result = ""
    tokens = ".?:"
    token_encoutered = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char.isspace() and token_encoutered:
            continue
        token_encoutered = False
        result += char
        if char in tokens:
            result += "\n\n"
            token_encoutered = True
    if token_encoutered:
        print(result, end="")
    else:
        print(result)
