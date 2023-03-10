"""You are given an array of non-negative integers numbers.
You are allowed to choose any number from this array and swap
any two digits in it. If after the swap operation the number
contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

Your task is to check whether it is possible to apply the swap
operation at most once, so that the elements of the resulting array are strictly increasing.
For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.

The initial array is already strictly increasing, so no actions are required.

For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.

By choosing numbers[2] = 900 and swapping its first and third digits,
the resulting number 009 is considered to be just 9.
So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

For numbers = [13, 31, 30], the output should be solution(numbers) = false.
"""


def solution(numbers):
    if numbers == sorted(numbers):
        return True

    def number_to_reverse(arr):
        for i in range(1, len(arr) - 1):
            if numbers[i] > numbers[i + 1]:
                return numbers[i]

    def is_strictly_increasing(arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True

    max_value = max(numbers)
    pivot = number_to_reverse(numbers)
    reversed_number = str(pivot)[::-1]
    reversed_number2 = str(max_value)[::-1]

    for i in range(len(numbers)):
        if pivot:
            if numbers[i] == pivot:
                numbers[i] = int(reversed_number)
        else:
            if numbers[i] == max_value:
                numbers[i] = int(reversed_number2)

    return is_strictly_increasing(numbers)


numbers = [1000, 10, 100]
print(solution(numbers))
