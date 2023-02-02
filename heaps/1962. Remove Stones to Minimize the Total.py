import heapq


def minStoneSum(piles, k):
    heap = [-i for i in piles]
    heapq.heapify(heap)

    while k != 0:
        heapq.heapreplace(heap, heap[0] // 2)
        k -= 1
    return -sum(heap)


piles = [5, 4, 9]
k = 2
print(minStoneSum(piles, k))
