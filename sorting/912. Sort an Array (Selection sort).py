def sortArray(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_num = i
        for j in range(min_num + 1, len(nums)):
            if nums[j] < nums[min_num]:
                min_num = j
        nums[i], nums[min_num] = nums[min_num], nums[i]
    return nums


nums = [5, 2, 3, 1]
print(sortArray(nums))
