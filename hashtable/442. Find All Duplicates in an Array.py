from collections import Counter


def findDuplicates(nums):
    count = Counter(nums)
    output = []
    for k, v in count.items():
        if v == 2:
            output.append(k)
    return output


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))
