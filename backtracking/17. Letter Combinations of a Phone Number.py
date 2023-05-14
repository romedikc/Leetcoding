def letterCombinations(digits: str) -> List[str]:
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        # if built string is == digits, we append and return
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        # building string
        for c in digitToChar[digits[i]]:
            # incrementing i cuz moving to the next digit
            # adding to current string the char we're visiting
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res


digits = "23"
print(letterCombinations(digits))
