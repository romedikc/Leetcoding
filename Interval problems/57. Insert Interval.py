def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    output = []
    for i in range(len(intervals)):
        # compare end of NI with the start of curr In for overlapping
        if newInterval[1] < intervals[i][0]:
            output.append(newInterval)
            return output + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
            # there is overlap
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    output.append(newInterval)
    return output


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(insert(intervals, newInterval))
