i = 0
def magic_string():
    global i
    return ", ".join(["BestSchool"] * (i := i + 1))
