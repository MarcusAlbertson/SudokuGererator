from random import shuffle


class Generator:
    """Creates filled valid 9x9 grid using random numbers, then removes numbers to create puzzle.

    Returns puzzle and solution
    """

    def __init__(self, grid=None):
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.solution_counter = 0
        self.generate()

    @staticmethod
    def get_empty_square(grid):
        """Input is a 9*9 grid. Finds locations on the grid that are empty (contain 0)

        Returns the next empty square (the ones containing 0) as a tuple."""
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] == 0:
                    return i, j

    @staticmethod
    def get_filled_squares(grid):
        """From the grid, this function find the squares that contain numbers (non 0s)

        returns a shuffled list of all squares that are filled with a number"""
        filled_square_lst = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] != 0:
                    filled_square_lst.append((i, j))
        shuffle(filled_square_lst)
        return filled_square_lst

    @staticmethod
    def is_num_in_sub(grid, row, col, num):
        """Finds whether a number has been using in a 3x3 sub Matrix

        Returns true if the number has already been used in the 3x3 sub matrix and false otherwise."""
        srow = 3 * (row // 3)
        scol = 3 * (col // 3)
        for i in range(srow, (srow + 3)):
            for j in range(scol, (scol + 3)):
                if grid[i][j] == num:
                    return True
                return False

    @staticmethod
    def is_num_in_row(grid, row, num):
        """Finds whether a number has been used in a specific row

        Returns true if the number is already in that row and false if it isn't"""
        if num in grid[row]:
            return True
        else:
            return False

    @staticmethod
    def is_num_in_column(grid, col, num):
        """Finds whether a number has been using in a specific column

        returns True if the number is already in that column and false if it isn't"""
        for i in range(0, 9):
            if grid[i][col] == num:
                return True
        return False

    def is_valid(self, grid, row, col, num):
        """combines the static methods to determine if the number's location is valid

        returns false if the number has been used in the row column or sub matrix"""
        if self.is_num_in_row(grid, row, num) == True:
            return False
        elif self.is_num_in_column(grid, col, num) == True:
            return False
        elif self.is_num_in_sub(grid, row, col, num) == True:
            return False
        else:
            return True

    def full_solution(self, grid):
        """Uses backtracking and the random shuffle function to randomly
        place integers 1 through 9 in the empty grid and backtrack until
        there is a full solution

        Returns a completed grid"""
        num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num_lst)
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:  # finding empty cells, then appends a num from num_lst if it is a valid location
                for num in num_lst:
                    if self.is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if not self.get_empty_square(grid):
                            return True
                        else:  # If grid is full of numbers solution has been found and break
                            if self.full_solution(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def solve(self, grid):
        """Takes input grid containing 0s as empty squares and numbers as filled squares,
         and counts the amount of valid ways a grid can be completed"""
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:  # finds empty cell, then trys numbers and if they are valid replaces the cell
                for num in range(0, 10):
                    if self.is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if not self.get_empty_square(grid):  # makes sure there is just one solution
                            self.solution_counter += 1
                            break
                        else:
                            if self.solve(grid):
                                return True
                break
        grid[row][col] = 0

    def remove_numbers_from_grid(self):
        """User inputs a difficultly setting. Based on that difficulty setting,
        a certain amount of numbers is removed from the complete grid, creating a puzzle.
        Solution counter is check to insure there is just one solution. If not, backtracks.

        Returns a solvable puzzle with one solution"""
        filled_squares = self.get_filled_squares(self.grid)
        filled_squares_count = len(filled_squares)
        a = input('What difficulty would you like (easy, medium, or hard?) ')  # setting the value for how many
        # squares will stay filled
        if a == 'easy':
            b = 60
        elif a == 'medium':
            b = 40
        elif a == 'hard':
            b = 22
        while filled_squares_count >= b:  # starts with 81 filled squares then removes numbers until there are b
            # filled squares
            row, col = filled_squares.pop()  # removes numbers and replaces them with ' '
            filled_squares_count -= 1
            self.grid[row][col] = ' '
            removed_square = self.grid[row][col]
            self.solution_counter = 0
            self.solve(self.grid)  # uses the solve function to determine how many solutions there are
            if self.solution_counter != 1:  # if there is not one solution, replace the number, add it back to the
                # filled
                # square count and move to the next cell
                self.grid[row][col] = removed_square
                filled_squares_count += 1

    def print(self, name):
        """This function simply prints the name of the grid, which is the
        parameter of the function, followed by the actual matrix"""
        print(name)
        for row in self.grid:
            print(row)

    def generate(self):
        """the function generates a full solution and prints it using the print function, then removes numbers
        from it and prints the new puzzle"""
        self.full_solution(self.grid)
        self.print('Full Solution:')
        self.remove_numbers_from_grid()
        self.print('Puzzle:')
