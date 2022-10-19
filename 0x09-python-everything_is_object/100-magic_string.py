#!/usr/bin/python3
i = 0
def magic_string(): return (lambda: ((globals().update(i=i + 1)),
                                     ", ".join(["BestSchool"] * (i))))()[1]
