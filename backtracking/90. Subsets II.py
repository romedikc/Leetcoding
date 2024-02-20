def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()

    subset = []
    output = []

    def backtracking(i):
        if i >= len(nums):
            output.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        backtracking(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtracking(i + 1)

    backtracking(0)
    return output


nums = [1, 2, 2]
print(subsetsWithDup(nums))
