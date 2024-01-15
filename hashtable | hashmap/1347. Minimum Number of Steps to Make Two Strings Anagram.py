def minSteps(s: str, t: str) -> int:
    count = 0
    s_freq = Counter(s)
    t_freq = Counter(t)

    if s_freq == t_freq:
        return 0

    for char in set(s + t):
        count += abs(s_freq[char] - t_freq[char])

    return count // 2


s = "leetcode"
t = "practice"
print(minSteps(s, t))
