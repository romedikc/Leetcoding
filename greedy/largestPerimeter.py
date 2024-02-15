def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    output = -1
    total = 0

    for n in nums:
        if total > n:
            output = total + n
        total += n

    return output


nums = [1, 12, 1, 2, 5, 50, 3]
print(largestPerimeter(nums))
