def minSubArrayLen(target: int, nums: List[int]) -> int:
    l = r = 0
    window_sum = 0  # sum of the current window
    min_sub = len(nums) + 1  # len of nums cuz we're looking for min not max
    while r < len(nums):
        window_sum += nums[r]  # add the current element to the sum of the window
        r += 1
        while window_sum >= target:
            min_sub = min(min_sub, r - l)
            window_sum -= nums[l]
            l += 1
    return min_sub if min_sub <= len(nums) else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]

print(minSubArrayLen(target, nums))
