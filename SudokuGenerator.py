def get_empty_squares(grid):
    """Input is a 9*9 grid and returns the next empty square (the ones containing 0)
    as a tuple."""
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return i, j
    return


def is_num_in_3by3(grid, row, col, num,):
    """Function is used to determain if a number has been used in a 3x3
    sub-matrix"""
    threecol = (col // 3) * 3
    threerow = (row // 3) * 3
    for i in range((threecol), (threecol+3)):
        for j in range (threerow, (threerow+3)):
            if grid[i][j]==num:
                return True
            else:
                return False


