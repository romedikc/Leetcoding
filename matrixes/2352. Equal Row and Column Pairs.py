def equalPairs(grid: List[List[int]]) -> int:
    count = 0
    row_counter = Counter()
    col_counter = Counter()

    for row in range(len(grid)):
        row_counter[tuple(grid[row])] += 1

    for col in range(len(grid[0])):
        column = [grid[row][col] for row in range(len(grid))]
        col_counter[tuple(column)] += 1

    for k in row_counter.keys():
        if k in col_counter:
            count += row_counter[k] * col_counter[k]
    return count


grid = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
print(equalPairs(grid))
