def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    count = 0
    l, r = 0, 0
    product = 1
    while r < len(nums):
        product *= nums[r]
        while product >= k and l <= r:
            product /= nums[l]
            l += 1
        count += r - l + 1
        r += 1
    return count


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))
