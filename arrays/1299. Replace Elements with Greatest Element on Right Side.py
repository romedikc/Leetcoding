from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    max_so_far = -1
    i = len(arr) - 1
    while i >= 0:
        temp = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, temp)
        i -= 1
    return arr


arr = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr))
