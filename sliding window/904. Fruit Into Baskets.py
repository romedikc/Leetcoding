def totalFruit(fruits: List[int]) -> int:
    l = r = 0
    max_sub = 0
    hashtable = Counter()
    distinct = 0
    while r < len(fruits):
        if hashtable[fruits[r]] == 0:
            distinct += 1
        hashtable[fruits[r]] += 1

        while distinct > 2:
            hashtable[fruits[l]] -= 1
            if hashtable[fruits[l]] == 0:
                distinct -= 1
            l += 1

        max_sub = max(max_sub, r - l + 1)
        r += 1
    return max_sub


fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(fruits))
