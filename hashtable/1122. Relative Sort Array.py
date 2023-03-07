from typing import List


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    not_seen = []
    arr1_copy = arr1.copy()

    for i in arr1_copy:
        if i not in arr2:
            not_seen.append(i)
            arr1.remove(i)

    not_seen.sort()
    sorting = sorted(arr1, key=lambda x: arr2.index(x))
    return sorting + not_seen


arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
arr2 = [2, 42, 38, 0, 43, 21]
print(relativeSortArray(arr1, arr2))
