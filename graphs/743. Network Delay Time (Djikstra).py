def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # adjacency list
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    min_heap = [(0, k)]  # weight and starting node
    visit = set()
    time = 0
    while min_heap:
        weight1, node1 = heapq.heappop(min_heap)
        if node1 in visit:  # if node is visited, just skip it
            continue
        visit.add(node1)
        time = max(time, weight1)
        # checking the neighbors of popped node1
        for node2, weight2 in edges[node1]:
            if node2 not in visit:
                # pushing total weight to reach node2
                heapq.heappush(min_heap, (weight1 + weight2, node2))
    return time if len(visit) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))
