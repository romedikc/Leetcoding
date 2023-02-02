def numSubarraysWithSum(nums, goal):
    # we store prefix sums based on current sum
    # prefix sum is 0:1 (o for the current sum, 1 for occurence of it)
    res, curr_sum, prefix_sums = 0, 0, {0: 1}
    # summing every number
    for n in nums:
        curr_sum += n
        # and substracting goal
        diff = curr_sum - goal
        # if there is a diff, we add to res the number of times
        # they occured
        res += prefix_sums.get(diff, 0)
        # incrementing the occurence of a curr_sum to prefix sum
        prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
    return res


nums = [1, 0, 1, 0, 1]
goal = 2
print(numSubarraysWithSum(nums, goal))
