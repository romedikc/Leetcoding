def canPlaceFlowers(flowerbed, n):
    i = 0
    while i < len(flowerbed) and n > 0:
        if flowerbed[i] == 0:
            prev = (i == 0) or (flowerbed[i - 1] == 0)
            next = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if prev and next:
                flowerbed[i] = 1
                n -= 1
        i += 1
    return n == 0


flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n))
