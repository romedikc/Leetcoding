def minSteps(s: str, t: str) -> int:
    s_freq = Counter(s)
    t_freq = Counter(t)
    return sum((s_freq - t_freq).values()) + sum((t_freq - s_freq).values())


s = "cotxazilut"
t = "nahrrmcchxwrieqqdwdpneitkxgnt"
print(minSteps(s, t))
