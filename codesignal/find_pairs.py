"""Given an array of unique integers numbers, your task is to find
the number of pairs of indices (i, j) such that i ≤ j
and the sum numbers[i] + numbers[j] is equal to some power of 2.

Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of 2.

Example

For numbers = [1, -1, 2, 3], the output should be solution(numbers) = 5.
There is one pair of indices where the corresponding elements sum up to 20 = 1:
(1, 2): numbers[1] + numbers[2] = -1 + 2 = 1
There are two pairs of indices where the corresponding elements sum up to 21 = 2:
(0, 0): numbers[0] + numbers[0] = 1 + 1 = 2
(1, 3): numbers[1] + numbers[3] = -1 + 3 = 2
There are two pairs of indices where the corresponding elements sum up to 22 = 4:
(0, 3): numbers[0] + numbers[3] = 1 + 3 = 4
(2, 2): numbers[2] + numbers[2] = 2 + 2 = 4
In total, there are 1 + 2 + 2 = 5 pairs summing up to powers of two."""


def solution(numbers):
    if len(numbers) == 1:
        return 1
    output = 0
    subarrays = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            subarrays.append([numbers[i], numbers[j]])
    for i in subarrays:
        s = sum(i)
        if s % 2 == 0:
            output += s
    return output - 1


# def solution(numbers):
#     output = 0
#     for i in range(0, len(numbers)):
#         for j in range(i, len(numbers)):
#             pair_sum = numbers[i] + numbers[j]
#             if not pair_sum & (pair_sum - 1) and pair_sum != 0:
#                 output += 1
#     return output


numbers = [1, -1, 2, 3]
print(solution(numbers))
