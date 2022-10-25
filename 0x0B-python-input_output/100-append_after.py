#!/usr/bin/python3
"""Search and update."""


def append_after(filename="", search_string="", new_string=""):
    """Append a line after each line containing a string in a file."""
    content = None
    with open(filename, "r", encoding="utf-8") as input_:
        content = input_.read()
    if content is None:
        return
    lines = content.split("\n")
    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)
    with open(filename, "w", encoding="utf-8") as output:
        output.write("".join(result))
