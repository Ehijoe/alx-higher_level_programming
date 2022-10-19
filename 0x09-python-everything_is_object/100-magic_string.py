#!/usr/bin/python3
i = 0
magic_string = lambda: (lambda: ((globals().update(i=i + 1)),
                                 ", ".join(["BestSchool"] * (i))))()[1]
