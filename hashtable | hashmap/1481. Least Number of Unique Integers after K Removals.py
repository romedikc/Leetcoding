def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    freq = Counter(arr)
    sorted_dict = sorted(freq.items(), key=lambda item: item[1])
    count = len(sorted_dict)
    for key, v in sorted_dict:
        if k >= v:
            k -= v
            count -= 1
        else:
            v = count
    return count


arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(findLeastNumOfUniqueInts(arr, k))
