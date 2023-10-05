def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    adj = collections.defaultdict(list)
    for i in range(n):
        adj[manager[i]].append(i)

    q = deque([(headID, 0)])  # head, time
    count = 0
    while q:
        id, time = q.popleft()
        count = max(count, time)
        for emp in adj[id]:
            q.append((emp, time + informTime[id]))
    return count


n = 1
headID = 0
manager = [-1]
informTime = [0]
print(numOfMinutes(n, headID, manager, informTime))
