def maxScore(nums: List[int]) -> int:
    nums.sort(reverse=True)
    prefix_sum = [0] * (len(nums) + 1)
    count = 0
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    for j in prefix_sum:
        if j > 0:
            count += 1
    return count


nums = [2, -1, 0, 1, -3, 3, -3]
print(maxScore(nums))
