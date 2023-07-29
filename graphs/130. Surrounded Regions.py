def solve(board: List[List[str]]) -> None:
    rows, cols = len(board), len(board[0])

    def capture(r, c):
        if (
                r < 0 or c < 0 or
                r == rows or c == rows or
                board[r][c] != "O"
        ):
            return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(c + 1, r)
        capture(c - 1, r)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(rows):
        for c in range(cols):
            if (
                    board[r][c] == "O" and
                    r in [0, rows - 1] or
                    c in [0, cols - 1]
            ):
                capture(r, c)

    # 2. Capture surrounded regions (O -> X)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "X":
                board[r][c] = "O"

    # 3. Uncapture unsurrounded regions (T -> O)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "T":
                board[r][c] = "O"


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(solve(board))
