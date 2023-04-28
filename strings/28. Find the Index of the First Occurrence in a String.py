def strStr(haystack: str, needle: str) -> int:
    i = 0
    while i < len(haystack) - len(needle) + 1:
        if haystack[i:i + len(needle)] == needle:
            return i
        else:
            i += 1
    return -1


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
