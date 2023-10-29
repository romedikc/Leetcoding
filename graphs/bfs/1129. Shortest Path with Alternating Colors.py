def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    red = collections.defaultdict(list)
    blue = collections.defaultdict(list)

    for src, dst in redEdges:
        red[src].append(dst)
    for src, dst in blueEdges:
        blue[src].append(dst)

    output = [-1] * n
    q = deque()
    q.append([0, 0, None])  # node, len, prev edge color
    visit = set()  # node, color
    visit.add((0, None))

    while q:
        node, lenght, color = q.popleft()
        if output[node] == -1:
            output[node] = lenght

        if color != "RED":
            for nei in red[node]:
                if (nei, "RED") not in visit:
                    visit.add((nei, "RED"))
                    q.append([nei, lenght + 1, "RED"])
        if color != "BLUE":
            for nei in blue[node]:
                if (nei, "BLUE") not in visit:
                    visit.add((nei, "BLUE"))
                    q.append([nei, lenght + 1, "BLUE"])
    return output


n = 3
redEdges = [[0, 1], [1, 2]]
blueEdges = []
print(shortestAlternatingPaths(n, redEdges, blueEdges))
