def orangesRotting(grid: List[List[int]]) -> int:
    # Initialize fresh oranges and time variables
    fresh, time = 0, 0
    # Create a queue for BFS
    q = deque()
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell contains a fresh orange (1), increment the fresh count
            if grid[r][c] == 1:
                fresh += 1
            # If the cell contains a rotten orange (2), add its position to the queue
            if grid[r][c] == 2:
                q.append([r, c])

    # Define directions for moving (up, down, left, right)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # Perform BFS while the queue is not empty and there are still fresh oranges
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()

            # Check each direction to see if there's a fresh orange to rot
            for dr, dc in directions:
                row, col = dr + r, dc + c
                # Check if the position is out of bounds or not a fresh orange
                if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                    continue
                # Mark the orange as rotten (2) and add its position to the queue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
            # Increment the time as we process each level of rotten oranges
        time += 1
    # Return the time taken to rot all oranges, or -1 if there are remaining fresh oranges
    return time if fresh == 0 else -1


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting(grid))
