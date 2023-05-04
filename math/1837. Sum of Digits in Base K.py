def sumBase(n: int, k: int) -> int:
    res = ''
    while n > 0:
        remainder = n % k
        res = str(remainder) + res
        n //= k
    return sum([int(i) for i in res])


n = 34
k = 6
print(sumBase(n, k))
