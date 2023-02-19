"""You are given two arrays of integers a and b of the same length,
and an integer k. We will be iterating through array
a from left to right, and simultaneously through array
b from right to left, and looking at pairs (x, y),
where x is from a and y is from b. Such a pair
is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll
encounter during the simultaneous iteration through a and b."""


def solution(a, b, k):
    count = 0
    b = b[::-1]
    i, j = 0, 0
    while i < len(a) and j < len(b):
        conc = str(a[i]) + str(b[j])
        if int(conc) < k:
            count += 1
        i += 1
        j += 1
    return count


a = [1, 2, 3]
b = [1, 2, 3]
k = 32
print(solution(a, b, k))
