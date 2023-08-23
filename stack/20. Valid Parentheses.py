import heapq
from collections import Counter
from typing import List


def isValid(s: str) -> bool:
    stack = []
    characters = {")": "(", "}": "{", "]": "["}
    for c in s:
        # if character is in characters, then it is closing one
        if c in characters:
            if stack and stack[-1] == characters[c]:
                stack.pop()
            else:
                return False
        # if we get an opening character, then append it to the stack
        else:
            stack.append(c)

    return True if not stack else False
