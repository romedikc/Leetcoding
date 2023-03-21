def checkInclusion(s1: str, s2: str) -> bool:
    for s in range(len(s2) - len(s1) + 1):
        window = s2[s:s + len(s1)]
        if ''.join(sorted(window)) == ''.join(sorted(s1)):
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))

""" if both strings sorted in lexicographic order 
and are equal, then s1 is a permutation of s2"""
