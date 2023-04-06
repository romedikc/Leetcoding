def addSpaces(s: str, spaces: List[int]) -> str:
    # 1 solution
    chars = list(s)
    new_s = ""
    i = 0
    while i < len(chars):
        if i in spaces:
            new_s += " "
        new_s += chars[i]
        i += 1
    return new_s

    # 2 solution
    chars = list(s)
    new_s = ""
    for i in range(len(chars)):
        if i in spaces:
            new_s += " "
        new_s += chars[i]
    return new_s


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
print(addSpaces(s, spaces))
