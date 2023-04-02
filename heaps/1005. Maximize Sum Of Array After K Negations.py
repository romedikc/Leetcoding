def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    for _ in range(k):
        heapq.heapreplace(nums, -nums[0])
    return sum(nums)


nums = [4, 2, 3]
k = 1
print(largestSumAfterKNegations(nums), k)
