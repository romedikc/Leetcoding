import heapq


def maxSubsequence(nums, k):
    heap = [(-nums[i], i) for i in range(len(nums))]
    heapq.heapify(heap)
    output = []
    while len(output) != k:
        output.append(heapq.heappop(heap))
    # returns the second element of the tuple,
    # which is the index of the element in nums.
    # So, the sort method will use the index of the element
    # in the original list to sort the output list.
    output.sort(key=lambda index: index[1])
    # applies the negation operation on the first element
    # of each element, which is a tuple of the form (-nums[i], i)
    return [-val[0] for val in output]


nums = [2, 1, 3, 3]
k = 2
print(maxSubsequence(nums, k))
