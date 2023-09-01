def sortArray(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1  # starting from 0

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


nums = [5, 2, 3, 1]
print(sortArray(nums))
