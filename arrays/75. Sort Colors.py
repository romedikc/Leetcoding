from typing import List


def sortColors(nums: List[int]) -> None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
