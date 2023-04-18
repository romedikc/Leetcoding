def vowelStrings(words: List[str], left: int, right: int) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(left, right + 1):
        word = words[i]
        if word[0] in vowels and word[-1] in vowels:
            count += 1
    return count


words = ["are", "amy", "u"]
left = 0
right = 2
print(vowelStrings(words, left, right))
