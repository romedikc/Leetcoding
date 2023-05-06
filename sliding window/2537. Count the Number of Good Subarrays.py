def countGood(nums: List[int], k: int) -> int:
    output = 0
    count = 0
    freq = Counter()
    l, r = 0, 0

    while r < len(nums):
        freq[nums[r]] += 1
        if freq[nums[r]] > 1:
            count += freq[nums[r]] - 1

        while count >= k:
            output += len(nums) - r
            if freq[nums[l]] > 1:
                count -= freq[nums[l]] - 1
            freq[nums[l]] -= 1

            l += 1
        r += 1
    return output


nums = [3, 1, 4, 3, 2, 2, 4]
k = 2
print(countGood(nums, k))
