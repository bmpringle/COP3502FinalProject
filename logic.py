import math, random
from enum import Enum

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for row in self.board:
            print("|", " ".join(row), "|")


    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for row in self.board:
            if num == row[col]:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        return sum([num in self.board[row][col_start:col_start + 3] for row in range(row_start, row_start + 3)]) == 0
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row // self.box_length * self.box_length, col // self.box_length * self.box_length, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        available_digits = list(range(1, self.row_length + 1))
        for row_offset in range(3):
            for col_offset in range(3):
                self.board[row_start + row_offset][col_start + col_offset] = available_digits.pop(random.randint(0, len(available_digits) - 1))
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        non_removed_cells = list(range(self.row_length ** 2))
        removed_cell_count = 0

        while removed_cell_count < self.removed_cells:
            remove_cell_index = non_removed_cells.pop(random.randint(0, len(non_removed_cells) - 1))
            self.board[remove_cell_index // self.row_length][remove_cell_index % self.row_length] = 0
            removed_cell_count += 1
        

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    solved_board = [row[:] for row in sudoku.get_board()] # This creates a copy of the board; 
    sudoku.remove_cells()
    starting_board = sudoku.get_board()
    return starting_board, solved_board

class Cell:
    def __init__(self, val):
        self.value = val
        self.sketched_value = 0

    def get(self):
        return self.value
    
    def get_sketched(self):
        return self.sketched_value
    
    def confirm_value(self):
        if self.can_edit_cell():
            self.value = self.sketched_value
            self.sketched_value = 0
            return True
        return False

    def set(self, val) -> bool:
        if self.can_edit_cell():
            self.sketched_value = val
            return True
        else:
            return False
    
    def can_edit_cell(self):
        return self.value == 0

class BoardCompletionState(Enum):
    INCOMPLETE = 1,
    WON = 2,
    LOST = 3

class Board:
    current_board : list[list[Cell]]
    solved_board : list[list[int]]

    def __init__(self, starting_board, solved_board) -> None:
        self.current_board = [[Cell(val) for val in row] for row in starting_board]
        self.solved_board = solved_board
    
    def sketch_value_in_cell(self, val, row, col):
        return self.current_board[row][col].set(val)
    
    def confirm_sketch(self, row, col):
        return self.current_board[row][col].confirm_value()
    
    def game_complete(self) -> bool:
        final_board = [[cell.get() for cell in row] for row in self.current_board]
        
        for row in final_board:
            if 0 in row:
                return BoardCompletionState.INCOMPLETE
        if final_board == self.solved_board:   
            return BoardCompletionState.WON
        
        return BoardCompletionState.LOST
    
            

    

    
