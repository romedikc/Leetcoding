"""Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such
that the sum of each pair is divisible by k.
"""


def solution(a, k):
    count = 0
    remainders = {}
    for i in range(len(a)):
        remainder = a[i] % k
        if (k - remainder) % k in remainders:
            count += remainders[(k - remainder) % k]

        if remainder in remainders:
            remainders[remainder] += 1
        else:
            remainders[remainder] = 1

    return count


a = [1, 2, 3, 4, 5]
k = 3
print(solution(a, k))
