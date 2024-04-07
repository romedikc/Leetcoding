def checkValidString(s: str) -> bool:
    low = 0  # Lower bound of number of '('
    high = 0  # Upper bound of number of '('

    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            if low > 0:
                low -= 1
            high -= 1
        else:  # c == '*'
            if low > 0:
                low -= 1
            high += 1

        if high < 0:
            return False  # More ')' than '(' and '*'

    return low == 0


s = "(*))"
print(checkValidString(s))
