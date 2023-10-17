def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    N = len(grid)
    q = deque([(0, 0, 1)])
    visit = set((0, 0))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]

    while q:
        r, c, length = q.popleft()
        if min(r, c) < 0 or max(r, c) >= N or grid[r][c]:
            continue
        # reached the end
        if r == N - 1 and c == N - 1:
            return length
        for dr, dc in directions:
            if (dr + r, dc + c) not in visit:
                q.append((dr + r, dc + c, length + 1))
                visit.add((dr + r, dc + c))
    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))
