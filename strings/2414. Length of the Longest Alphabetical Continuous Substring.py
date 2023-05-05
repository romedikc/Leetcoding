def longestContinuousSubstring(self, s: str) -> int:
    count = 1
    longest = 1
    for i in range(len(s) - 1):
        if ord(s[i + 1]) - ord(s[i]) == 1:
            count += 1
        else:
            count = 1
        longest = max(longest, count)
    return longest


s = "abacaba"
print(longestContinuousSubstring(s))
