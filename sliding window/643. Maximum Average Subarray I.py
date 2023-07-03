def findMaxAverage(nums: List[int], k: int) -> float:
    l, r = 0, 0
    curr_sum, max_avg = 0, float('-inf')

    while r < len(nums):
        curr_sum += nums[r]

        if r - l + 1 == k:
            max_avg = max(max_avg, curr_sum / k)
            curr_sum -= nums[l]
            l += 1
        r += 1
    return max_avg


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))
