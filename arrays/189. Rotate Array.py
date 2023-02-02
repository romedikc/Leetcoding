def rotate(nums, k):
    # so k not > len of nums
    k = k % len(nums)
    l, r = 0, len(nums) - 1

    # first we reverse an entire array
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # reverse first K elements
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # reverse remaining portion of an array
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))
