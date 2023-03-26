def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    even_sum = sum(n for n in nums if n % 2 == 0)
    output = []
    for v, i in queries:
        # check before adding a new value
        if nums[i] % 2 == 0:
            even_sum -= nums[i]
        nums[i] += v
        # checks if a new added value is even
        if nums[i] % 2 == 0:
            even_sum += nums[i]
        output.append(even_sum)
    return output


nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sumEvenAfterQueries(nums, queries))
