from collections import Counter


def checkRecord(s: str) -> bool:
    freq = Counter(s)
    for k, v in freq.items():
        if k == 'A' and v >= 2:
            return False
        elif k == 'L' and 'LLL' in s:
            return False

    return True


s = "PPALLL"
print(checkRecord(s))
