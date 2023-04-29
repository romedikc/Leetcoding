def repeatedSubstringPattern(s: str) -> bool:
    return s in s[1:] + s[:-1]


s = "abab"
print(repeatedSubstringPattern(s))
