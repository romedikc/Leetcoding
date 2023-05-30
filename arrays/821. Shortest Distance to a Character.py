def shortestToChar(s: str, c: str) -> List[int]:
    c_indexes = [index for index, char in enumerate(s) if char == c]
    output = []
    for i in range(len(s)):
        distances = [abs(i - index) for index in c_indexes]
        output.append(min(distances))
    return output


s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
