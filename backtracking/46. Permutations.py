def permute(nums: List[int]) -> List[List[int]]:
    output = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        output.extend(perms)
        nums.append(n)
    return output


nums = [1, 2, 3]
print(permute(nums))
