def findKthLargest(nums: List[int], k: int) -> int:
    def partition(nums, l, r):
        pivot, pointer = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[r] = nums[r], nums[pointer]

        return pointer  # rightmost element after partition

    k = len(nums) - k
    l, r = 0, len(nums) - 1
    while l < r:
        pivot = partition(nums, l, r)
        if pivot < k:
            l = pivot + 1
        elif pivot > k:
            r = pivot - 1
        else:
            break
    return nums[k]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
