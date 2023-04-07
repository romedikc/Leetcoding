def equalSubstring(s: str, t: str, maxCost: int) -> int:
    l = r = 0
    max_len = 0
    cost = 0
    while r < len(s):
        cost += abs(ord(s[r]) - ord(t[r]))
        r += 1

        while cost > maxCost:
            cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        max_len = max(max_len, r - l)

    return max_len


s = "abcd"
t = "bcdf"
maxCost = 3

print(equalSubstring(s, t, maxCost))
