def minNumber(nums1: List[int], nums2: List[int]) -> int:
    output = []
    for i in nums1:
        if i in nums2:
            output.append(i)

    if not output:
        minimum1 = min(nums1)
        minimum2 = min(nums2)
        if minimum1 > minimum2:
            return int(str(minimum2) + str(minimum1))
        else:
            return int(str(minimum1) + str(minimum2))
    return min(output)


nums1 = [4, 1, 3]
nums2 = [5, 7]
print(minNumber(nums1, nums2))
