def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]  # it can't be 0 cuz there are negative nums in nums
    curr_sum = 0

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0  # we don't count negatives to maximize sum
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
