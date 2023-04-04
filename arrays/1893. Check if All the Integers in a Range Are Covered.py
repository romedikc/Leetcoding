def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    count = 0
    for i in range(left, right + 1):
        for r in ranges:
            if r[0] <= i <= r[1]:
                count += 1
                break
    return count == right - left + 1


ranges = [[1, 50]]
left = 1
right = 50
print(isCovered(ranges, left, right))
