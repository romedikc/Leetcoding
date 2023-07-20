import heapq
from collections import Counter
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    # trivial solution

    # potions.sort()  # Sort the potions list
    # output = []
    # i = 0
    #
    # while i < len(spells):
    #     j = 0
    #     count = 0
    #
    #     while j < len(potions):
    #         prod = potions[j] * spells[i]
    #         if prod >= success:
    #             count += len(potions) - j
    #             break  # Stop iterating if prod >= success is found
    #         j += 1
    #
    #     output.append(count)
    #     i += 1
    #
    # return output

    # binary search
    potions.sort()
    output = []
    for s in spells:
        l, r = 0, len(potions) - 1
        idx = len(potions)  # furthest left that works

        while l <= r:
            m = (l + r) // 2
            if s * potions[m] >= success:
                r = m - 1
                idx = m  # in case of duplicates we're keeping first found index
            else:
                l = m + 1
        output.append(len(potions) - idx)
    return output


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))
