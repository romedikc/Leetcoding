def countDistinctIntegers(nums):
    s = set(nums)
    for i in nums:
        s.add(int(str(i)[::-1]))
    return len(s)


nums = [1, 13, 10, 12, 31]
print(countDistinctIntegers(nums))
