def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sorting intervals by start
    intervals.sort(key=lambda pair: pair[0])
    # storing the 1st element to avoid edge case like index out of range
    output = [intervals[0]]
    for start, end in intervals[1:]:
        prevEnd = output[-1][1]  # end value of most resent added interval
        # if previous end num > than the starting of the next interval
        # we merge them
        if start <= prevEnd:
            # merge
            output[-1][1] = max(prevEnd, end)  # previous end and current end
        else:
            output.append([start, end])
    return output


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
