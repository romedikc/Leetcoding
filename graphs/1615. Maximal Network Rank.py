def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    adj = collections.defaultdict(list)
    for src, dst in roads:
        adj[src].append(dst)
        adj[dst].append(src)

    max_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            rank = len(adj[i]) + len(adj[j])
            if i in adj[j] or j in adj[i]:
                rank -= 1
            max_rank = max(max_rank, rank)
    return max_rank


n = 5
roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
print(maximalNetworkRank(n, roads))
