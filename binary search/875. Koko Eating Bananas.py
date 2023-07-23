def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    while l < r:
        mid = (l + r) // 2
        total_hours = sum(math.ceil(pile / mid) for pile in piles)

        if total_hours > h:
            l = mid + 1
        else:
            r = mid
    return l


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
