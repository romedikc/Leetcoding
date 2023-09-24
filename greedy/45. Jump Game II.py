def jump(nums: List[int]) -> int:
    l = r = 0
    count = 0
    while r < len(nums) - 1:
        furthest = 0
        for i in range(l, r + 1):
            furthest = max(furthest, i + nums[i])
        l = r + 1
        r = furthest
        count += 1
    return count


nums = [2, 3, 1, 1, 4]
print(jump(nums))
