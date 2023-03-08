from collections import Counter
from typing import List


def findLonely(nums: List[int]) -> List[int]:
    freq = Counter(nums)
    output = []
    for i in nums:
        if i + 1 not in freq and i - 1 not in freq and freq[i] == 1:
            output.append(i)
    return output


nums = [1, 3, 5, 3]
print(findLonely(nums))
