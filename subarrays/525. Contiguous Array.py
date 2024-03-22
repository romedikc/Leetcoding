def findMaxLength(nums: List[int]) -> int:
    diff_idx = {0: -1}
    max_len = 0
    one, zero = 0, 0

    for i, n in enumerate(nums):
        if n == 1:
            one += 1
        else:
            zero += 1
        diff = one - zero
        if diff in diff_idx:
            max_len = max(max_len, i - diff_idx[diff])
        else:
            diff_idx[diff] = i
    return max_len


nums = [0, 0, 1, 0, 0, 0, 1, 1]
print(findMaxLength(nums))
