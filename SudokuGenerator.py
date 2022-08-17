def get_empty_squares(grid):
    for i in range(0,9):
        for j in range (0,9):
            if grid[i][j]==0:
                return i,j
    return
