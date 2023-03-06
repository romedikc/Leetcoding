def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def letter_to_alphabet_value(string):
        values = []
        for l in string:
            ascii_value = ord(l.lower()) - 97
            values.append(ascii_value)
        return values

    string1 = [str(i) for i in letter_to_alphabet_value(firstWord)]
    string2 = [str(j) for j in letter_to_alphabet_value(secondWord)]
    target = [str(k) for k in letter_to_alphabet_value(targetWord)]

    join1 = ''.join(string1)
    join2 = ''.join(string2)
    join3 = ''.join(target)

    if int(join1) + int(join2) == int(join3):
        return True
    return False


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(isSumEqual(firstWord, secondWord, targetWord))
