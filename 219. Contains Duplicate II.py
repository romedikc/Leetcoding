def solution(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and abs(i - d[nums[i]]) <= k:
            return True
        d[nums[i]] = i
    return False


nums = [0, 1, 2, 3, 5, 2]
k = 3
print(solution(nums, k))
