def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    count = 0
    intervals.sort(key=lambda start: start[0])
    end_of_last_interval = float('-inf')

    for start, end in intervals:
        if start < end_of_last_interval:
            count += 1
            end_of_last_interval = min(end, end_of_last_interval)
        else:
            end_of_last_interval = end
    return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))
