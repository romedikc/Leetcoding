def minAddToMakeValid(s: str) -> int:
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)
    return len(stack)


s = "()))(("
print(minAddToMakeValid(s))
