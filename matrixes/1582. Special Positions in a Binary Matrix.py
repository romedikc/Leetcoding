def numSpecial(mat: List[List[int]]) -> int:
    row_counts = [0] * (len(mat))
    col_counts = [0] * (len(mat[0]))

    # counting 1s
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 1:
                row_counts[row] += 1
                col_counts[col] += 1

    count = 0
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 1 and row_counts[row] == 1 and col_counts[col] == 1:
                count += 1
    return count


mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
print(numSpecial(mat))
