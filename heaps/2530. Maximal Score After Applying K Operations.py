import heapq
from math import ceil


def maxKelements(nums, k):
    heap = [-i for i in nums]
    heapq.heapify(heap)
    total = 0
    while k != 0:
        greatest = heapq.heappop(heap)
        total += greatest
        heapq.heappush(heap, ceil(greatest // 3))
        k -= 1
    return -total


nums = [1, 10, 3, 3, 3]
k = 3
print(maxKelements(nums, k))
