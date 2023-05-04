def dailyTemperatures(temperatures: List[int]) -> List[int]:
    output = [0] * (len(temperatures))
    stack = []
    for i, v in enumerate(temperatures):
        while stack and v > stack[-1][0]:
            stack_value, stack_index = stack.pop()
            output[stack_index] = (i - stack_index)
        stack.append([v, i])

    return output


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))
