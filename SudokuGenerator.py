from random import shuffle


class Generator:

    @staticmethod
    def get_empty_square(grid):
        """Input is a 9*9 grid and returns the next empty square (the ones containing 0)
                as a tuple."""
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] == 0:
                    return i, j

    @staticmethod
    def is_num_in_sub(grid, row, col, num):
        """Returns true if the number has already been used in the 3x3 sub matrix and false otherwise."""
        srow = 3 * (row // 3)
        scol = 3 * (col // 3)
        for i in range(srow, (srow + 3)):
            for j in range(scol, (scol + 3)):
                if grid[i][j] == num:
                    return True
                return False

    @staticmethod
    def is_num_in_row(grid, row, num):
        """Returns true if the number is already in that row and false if it isn't"""
        if num in grid[row]:
            return True
        else:
            return False

    @staticmethod
    def is_num_in_column(grid, col, num):
        """returns True if the number is already in that column and false if it isn't"""
        for i in range(0, 9):
            if grid[i][col] == num:
                return True
        return False

    @staticmethod
    def get_filled_squares(grid):
        """From the grid, this function returns a shuffled list of all squares
        that are filled with a number"""
        filled_square_lst = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] != 0:
                    filled_square_lst.append((i, j))
        shuffle(filled_square_lst)
        return filled_square_lst
