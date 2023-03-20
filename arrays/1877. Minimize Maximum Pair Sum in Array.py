def minPairSum(nums: List[int]) -> int:
    max_heap = [-i for i in nums]
    heapq.heapify(max_heap)
    heapq.heapify(nums)  # min heap
    output = []
    n = len(nums)
    while n:
        max_value = -heapq.heappop(max_heap)
        min_value = heapq.heappop(nums)
        output.append(max_value + min_value)
        n -= 2
    return max(output)


nums = [4, 1, 5, 1, 2, 5, 1, 5, 5, 4]
print(minPairSum(nums))
