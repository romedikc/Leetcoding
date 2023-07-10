def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == "*":
            if stack:
                stack.pop()  # Remove the character before *
        else:
            stack.append(ch)  # Push the character onto the stack
    return ''.join(stack)


s = "erase*****"
print(removeStars(s))
