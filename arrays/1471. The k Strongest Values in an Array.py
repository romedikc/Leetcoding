def getStrongest(arr: List[int], k: int) -> List[int]:
    arr.sort()
    m = arr[(len(arr) - 1) // 2]
    output = []
    l, r = 0, len(arr) - 1
    while l <= r:
        if abs(arr[l] - m) > abs(arr[r] - m):
            output.append(arr[l])
            l += 1
        else:
            output.append(arr[r])
            r -= 1
    return output[:k]


arr = [1, 2, 3, 4, 5]
k = 2
print(getStrongest(arr, k))
