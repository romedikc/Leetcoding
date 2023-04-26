def frequencySort(nums: List[int]) -> List[int]:
    # count the frequency of each number in the array
    freq = Counter(nums)

    # sort the array based on the frequency and the value of each element
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x, nums.index(x)))

    return sorted_nums


nums = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums))
