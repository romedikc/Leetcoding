from typing import List


def checkXMatrix(grid: List[List[int]]) -> bool:
    for i in range(len(grid)):  # row
        for j in range(len(grid[0])):  # col
            # checking right and left diagonal
            if i == j or i == len(grid) - 1 - j:
                if grid[i][j] == 0:  # if a number in diagonal is 0 -> false
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True


grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
print(checkXMatrix(grid))
