def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    splt_s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] in vowels and s[r] in vowels:
            splt_s[l], splt_s[r] = splt_s[r], splt_s[l]
            l += 1
            r -= 1
        elif s[l] in vowels:
            r -= 1
        else:
            l += 1
    return ''.join(splt_s)


s = "hello"
print(reverseVowels(s))
