def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    safe = {}

    def dfs(i):
        if i in safe:
            return safe[i]

        # looking for safe nodes / detecting cycles
        safe[i] = False
        for neigh in graph[i]:
            if not dfs(neigh):
                return False
        # if every neighbour is a safe node, then True
        safe[i] = True
        return safe[i]

    output = []
    for i in range(len(graph)):
        if dfs(i):
            output.append(i)
    return output


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(eventualSafeNodes(graph))
