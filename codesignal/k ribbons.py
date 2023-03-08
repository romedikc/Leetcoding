"""You are given an array of integers a, where each element
a[i] represents the length of a ribbon.

Your goal is to obtain k ribbons of the same length,
by cutting the ribbons into as many pieces as you want.

Your task is to calculate the maximum integer length L
for which it is possible to obtain at least
k ribbons of length L by cutting the given ones.

Example

For a = [5, 2, 7, 4, 9] and k = 5,
the output should be solution(a, k) = 4.
https://www.tutorialspoint.com/program-to-find-maximum-length-of-k-ribbons-of-same-length-in-python
"""


def solution(a, k):
    l, r = 0, max(a)
    while l < r:
        mid = (l + r + 1) // 2
        if sum((length // mid for length in a)) >= k:
            l = mid
        else:
            r = mid - 1
    if l:
        return l
    return -1


a = [5, 2, 7, 4, 9]
k = 5
print(solution(a, k))
