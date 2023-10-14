def minReorder(n: int, connections: List[List[int]]) -> int:
    tree = [[] for _ in range(n)]
    for a, b in connections:
        tree[a].append((b, 1))
        tree[b].append((a, 0))

    visited = set()

    def dfs(node):
        visited.add(node)
        count = 0
        for neigh, direc in tree[node]:
            if neigh not in visited:
                # Count outgoing edges
                # (1 indicates outgoing, 0 incoming)
                count += direc
                count += dfs(neigh)
        return count

    return dfs(0)


n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(minReorder(n, connections))
