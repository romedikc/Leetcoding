def decodeString(s: str) -> str:
    stack = []
    curr_str = ""
    curr_count = 0

    for c in s:
        if c.isdigit():
            curr_count = curr_count * 10 + int(c)  # Handle multi-digit numbers
        elif c == "[":
            stack.append((curr_count, curr_str))
            curr_count, curr_str = 0, ""  # Reset for the next inner bracket
        elif c.isalpha():
            curr_str += c
        else:
            count, prev_str = stack.pop()
            curr_str = prev_str + curr_str * count

    return curr_str


s = "3[a]2[bc]"
print(decodeString(s))
