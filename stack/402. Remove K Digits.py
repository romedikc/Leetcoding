def removeKdigits(num: str, k: int) -> str:
    stack = []
    removed = 0
    for n in num:
        while stack and removed < k and stack[-1] > n:
            stack.pop()
            removed += 1
        if n != "0" or stack:
            stack.append(n)
    while stack and removed < k:
        stack.pop()
        removed += 1
    return "".join(stack) if stack else "0"


num = "1432219"
k = 4
print(removeKdigits(num, k))
