"""You are given two strings - pattern and source.
The first string pattern contains only the symbols 0 and 1,
and the second string source contains only lowercase English letters.

Let's say that pattern matches a substring source[l..r] of source
if the following three conditions are met:

they have equal length,
for each 0 in pattern the corresponding letter in the substring is a vowel,
for each 1 in pattern the corresponding letter is a consonant.
Your task is to calculate the number of substrings of source that match pattern"""


def solution(pattern, source):
    def count_vowels_consonants(pattern):
        vowels = consonants = 0
        for p in pattern:
            if p == "0":
                vowels += 1
            else:
                consonants += 1
        return [vowels, consonants]

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    count = 0
    for k in range(len(source) - len(pattern) + 1):
        window = source[k:k + len(pattern)]
        sub_vowels, sub_consonants = 0, 0
        for i, c in enumerate(window):
            if pattern[i] == '0' and c in vowels:
                sub_vowels += 1
            elif pattern[i] == '1' and c not in vowels:
                sub_consonants += 1
        if [sub_vowels, sub_consonants] == count_vowels_consonants(pattern):
            count += 1

    return count


pattern = "010"
source = "amazing"
print(solution(pattern, source))
