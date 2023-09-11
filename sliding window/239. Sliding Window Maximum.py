def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    queue = deque()
    l = r = 0
    while r < len(nums):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)

        if l > queue[0]:
            queue.popleft()

        if (r + 1) >= k:
            output.append(nums[queue[0]])
            l += 1
        r += 1
    return output


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
