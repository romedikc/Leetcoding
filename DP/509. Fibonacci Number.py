def fib(n: int) -> int:
    num_0, num_1 = 0, 1
    for _ in range(n):
        num_0, num_1 = num_1, num_1 + num_0
    return num_0


n = 2
print(fib(n))
