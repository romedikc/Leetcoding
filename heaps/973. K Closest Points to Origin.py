def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    min_heap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        min_heap.append([dist, x, y])

    heapq.heapify(min_heap)
    output = []
    while k:
        dist, x, y = heapq.heappop(min_heap)
        output.append([x, y])
        k -= 1
    return output


points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))
