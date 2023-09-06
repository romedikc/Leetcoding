def findMin(nums: List[int]) -> int:
    output = nums[0]  # just any num
    l, r = 0, len(nums) - 1
    while l <= r:
        # in case if arr is already sorted
        if nums[l] < nums[r]:
            output = min(output, nums[l])
            break

        mid = (l + r) // 2
        output = min(output, nums[mid])
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return output


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
