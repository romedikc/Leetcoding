def leftRigthDifference(nums: List[int]) -> List[int]:
    prefix_sum = [0] * (len(nums))
    for i in range(len(nums) - 1):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    suffix_sum = [0] * len(nums)
    suffix_sum[len(nums) - 1] = 0
    for j in range(len(nums) - 1, -1, -1):
        if j == 0:
            break
        suffix_sum[j - 1] = suffix_sum[j] + nums[j]

    output = []
    for k in range(len(prefix_sum)):
        total = abs(prefix_sum[k] - suffix_sum[k])
        output.append(total)

    return output


nums = [10, 4, 8, 3]
print(leftRigthDifference(nums))
