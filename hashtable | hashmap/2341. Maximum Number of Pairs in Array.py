from typing import List


def numberOfPairs(nums: List[int]) -> List[int]:
    singles = set()
    mingles = 0
    for n in nums:
        if n in singles:
            singles.remove(n)
            mingles += 1
        else:
            singles.add(n)
    return [mingles, len(singles)]


nums = [1, 3, 2, 1, 3, 2, 2]
print(numberOfPairs(nums))
