from typing import List


def arrayChange(nums: List[int], operations: List[List[int]]) -> List[int]:
    index_map = {v: i for i, v in enumerate(nums)}
    for v in operations:
        if v[0] in nums:
            index = index_map[v[0]]
            nums[index] = v[1]
            index_map[v[0]] = -1  # marking old index as invalid
            index_map[v[1]] = index
    return nums


nums = [1, 2]
operations = [[1, 3], [2, 1], [3, 2]]
print(arrayChange(nums, operations))
