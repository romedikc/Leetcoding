def firstMissingPositive(nums: List[int]) -> int:
    max_num = abs(max(nums))
    for i in range(1, max_num + 1):
        if i not in nums:
            return i
    return max_num + 1


nums = [-5]
print(firstMissingPositive(nums))
