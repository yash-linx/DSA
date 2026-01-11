# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# Output: true

# board = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
from collections import defaultdict
def isValidSudoku(board: list[list[str]]) -> bool:
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    cube_dict = defaultdict(set)

    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]==".":
                continue
            if (board[row][column] in col_dict[column] or 
                board[row][column] in row_dict[row] or 
                board[row][column] in cube_dict[(row//3,column//3)]
                ):
                return False
            col_dict[column].add(board[row][column])
            row_dict[row].add(board[row][column])
            cube_dict[(row//3,column//3)].add(board[row][column])
    return True

print(isValidSudoku(board))
            