def minOperations(nums: List[int]) -> int:
    count = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            diff = nums[i - 1] - nums[i] + 1
            count += diff

            nums[i] += diff
    return count


nums = [1, 1, 1]
print(minOperations(nums))
