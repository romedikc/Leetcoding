def maximizeGreatness(nums: List[int]) -> int:
    count = 0
    nums.sort()
    for n in nums:
        if n > nums[count]:
            count += 1
    return count


nums = [1, 3, 5, 2, 1, 3, 1]
print(maximizeGreatness(nums))
