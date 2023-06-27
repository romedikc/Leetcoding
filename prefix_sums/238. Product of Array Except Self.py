def productExceptSelf(nums: List[int]) -> List[int]:
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    right = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):  # second-to-last index
        right[i] = right[i + 1] * nums[i + 1]

    output = []
    for i in range(len(nums)):
        output.append(left[i] * right[i])
    return output


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
