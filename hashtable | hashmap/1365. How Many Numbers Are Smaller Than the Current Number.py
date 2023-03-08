def smallerNumbersThanCurrent(nums):
    dic = {}
    for i, v in enumerate(sorted(nums)):
        if v not in dic:
            dic[v] = i
    return [dic[v] for v in nums]


nums = [6, 5, 4, 8]
print(smallerNumbersThanCurrent(nums))
