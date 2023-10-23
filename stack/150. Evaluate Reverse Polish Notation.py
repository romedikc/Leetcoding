def evalRPN(tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t == "+":
            stack.append(stack.pop() + stack.pop())
        elif t == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif t == "*":
            stack.append(stack.pop() * stack.pop())
        elif t == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(t))
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))
