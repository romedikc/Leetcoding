def canReach(arr: List[int], start: int) -> bool:
    q = deque([start])
    N = len(arr)
    i = start

    while q and arr[i] != 0:
        i = q.popleft()
        l, r = i - arr[i], i + arr[i]

        if l > -1 and arr[l] > -1:
            q.append(l)
        if r < N and arr[r] > -1:
            q.append(r)
        # mark visited
        arr[i] *= -1
    return arr[i] == 0


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(arr, start))
