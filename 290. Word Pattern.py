def solution(strings, patterns):
    if len(strings) != len(patterns):
        return False
    for i in range(len(strings) - 1):
        for j in range(i, len(strings)):
            check = strings[i] == strings[j]
            check2 = patterns[i] == patterns[j]
            if check != check2:
                return False
    return True


strings = ["a", "b", "a"]
patterns = ["c", "d", "d"]
print(solution(strings, patterns))
