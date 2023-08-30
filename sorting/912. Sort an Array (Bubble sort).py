def sortArray(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


nums = [5, 2, 3, 1]
print(sortArray(nums))
