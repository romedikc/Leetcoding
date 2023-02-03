from collections import Counter


def findAnagrams(s, p):
    len_p, len_s = len(p), len(s)
    indices = []
    for i in range(len_s - len_p + 1):
        window = s[i:i + len_p]
        if Counter(window) == Counter(p):
            indices.append(i)
    return indices


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
