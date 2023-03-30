def longestOnes(nums: List[int], k: int) -> int:
    l = r = 0
    zeros = max_ones = 0
    while r < len(nums):
        # If we encounter a 0, increment the number of zeros
        if nums[r] == 0:
            zeros += 1
        # If we have more than k zeros, move the left pointer forward
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        # Update the maximum number of consecutive 1's
        max_ones = max(max_ones, r - l + 1)
        r += 1
    return max_ones


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))
