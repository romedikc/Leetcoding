def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    lst = sentence.split(" ")
    for i in range(len(lst)):
        if lst[i][:len(searchWord)] == searchWord:
            return i + 1
    return -1


sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence, searchWord))
