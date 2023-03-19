def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    window = ""
    char_dict = {}
    for i in range(len(s)):
        if s[i] not in window:
            window += s[i]
            char_dict[s[i]] = i
        else:
            # Update the start index of the window to be the maximum of its
            # current value and the last index of the character in the window plus 1
            window = s[char_dict[s[i]] + 1:i + 1]
            char_dict[s[i]] = i
        max_len = max(max_len, len(window))
    return max_len


s = "pwwkew"
print(lengthOfLongestSubstring(s))
