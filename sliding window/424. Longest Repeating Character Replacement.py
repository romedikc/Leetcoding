def characterReplacement(s: str, k: int) -> int:
    l = r = 0
    freq = Counter()
    max_output = 0
    max_freq = 0  # Track the maximum frequency of any character in the window

    while r < len(s):
        freq[s[r]] += 1
        max_freq = max(max_freq, freq[s[r]])

        while (r - l + 1 - max_freq) > k:
            freq[s[l]] -= 1
            l += 1

        max_output = max(max_output, r - l + 1)
        r += 1

    return max_output


s = "ABAB"
k = 2
print(characterReplacement(s, k))
