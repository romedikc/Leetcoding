def findCircleNum(isConnected: List[List[int]]) -> int:
    count = 0
    visit = set()
    rows, cols = len(isConnected), len(isConnected[0])

    def dfs(start):
        for col in range(len(isConnected[start])):
            if isConnected[start][col] == 1 and col not in visit:
                visit.add(col)
                dfs(col)

    for r in range(rows):
        for c in range(cols):
            if isConnected[r][c] == 1 and c not in visit:
                visit.add(c)
                dfs(c)
                count += 1
    return count


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))
