def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    curr_sum = 0
    prefix_sums = Counter()
    # if the current sum is equal to k,
    # it contributes to the count of subarrays.
    prefix_sums[0] = 1

    for n in nums:
        curr_sum += n
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]

        prefix_sums[curr_sum] += 1
    return count


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))
# We iterate through the nums array, updating the curr_sum and checking if curr_sum - k exists in prefix_sums.
# If it does, we increment the count by the frequency of curr_sum - k in prefix_sums.
# We update the frequency of the current sum curr_sum in prefix_sums.
