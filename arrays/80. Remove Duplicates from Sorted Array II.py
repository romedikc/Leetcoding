def removeDuplicates(nums: List[int]) -> int:
    count = 1
    l = 1
    for r in range(1, len(nums)):
        if nums[r] == nums[r - 1]:
            count += 1
        else:
            count = 1  # Reset count when encountering a new number
        if count <= 2:
            nums[l] = nums[r]
            l += 1
    return l


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))
