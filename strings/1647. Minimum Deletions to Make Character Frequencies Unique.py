from collections import Counter


def minDeletions(s):
    freq = Counter(s)
    seen = set()
    count = 0
    for v in freq.values():
        while v > 0 and v in seen:
            count += 1
            v -= 1
        seen.add(v)
    return count


s = "ceabaacb"
print(minDeletions(s))
