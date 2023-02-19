"""Given an array of integers a, your task is to count
the number of pairs i and j (where 0 ≤ i < j < a.length),
such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams
if they contain the same digits. In other words,
one can be obtained from the other by rearranging
the digits (or trivially, if the numbers are equal).
For example, 54275 and 45572 are digit anagrams,
but 321 and 782 are not (since they don't contain the same digits).
220 and 22 are also not considered as digit anagrams,
since they don't even have the same number of digits."""

from collections import Counter


def solution(a):
    count = 0
    strings = [str(i) for i in a]
    freq = Counter()

    for s in strings:
        freq[tuple(sorted(s))] += 1

    for n in freq.values():
        count += (n * (n - 1)) // 2

    return count


a = [25, 35, 872, 228, 53, 278, 872]
print(solution(a))
