# 1 approach O(n^2)
def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    for i in range(len(s) - k + 1):
        window = s[i:i + k]
        count = 0

        for j in window:
            if j in vowels:
                count += 1
        max_vowels = max(count, max_vowels)
    return max_vowels


s = "abciiidef"
k = 3
print(maxVowels(s, k))

# 2 approach O(n)

"""
The expression i >= k checks if the current window has length k.
If it does, we can slide the window to the right by one character.
If it doesn't, we cannot slide the window any further to the right.
The expression s[i-k] in vowels checks if the character at index i-k
(i.e., the first character in the current window) is a vowel or not.
If it is a vowel, we decrement the count variable because
we are removing a vowel from the window.
"""


def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = count = 0
    for i in range(len(s)):
        if i >= k and s[i - k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_vowels = max(count, max_vowels)
    return max_vowels


s = "abciiidef"
k = 3
print(maxVowels(s, k))
