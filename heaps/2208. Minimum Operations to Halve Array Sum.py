import heapq
from typing import List


def halveArray(nums: List[int]) -> int:
    count = 0
    initial_sum = sum(nums)
    target = initial_sum / 2

    heap = [-i for i in nums]
    heapq.heapify(heap)

    while target < initial_sum:
        num = heapq.heappop(heap)
        heapq.heappush(heap, num / 2)
        initial_sum = initial_sum - abs(num) + abs(num / 2)
        count += 1
    return count


nums = [5, 19, 8, 1]
print(halveArray(nums))
