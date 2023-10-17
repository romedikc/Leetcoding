def longestConsecutive(nums: List[int]) -> int:
    hashSet = set(nums)
    longest_streak = 0

    for n in nums:
        if n - 1 not in hashSet:
            length = 0
            while n + length in hashSet:
                length += 1
            longest_streak = max(longest_streak, length)
    return longest_streak


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(longestConsecutive(nums))
