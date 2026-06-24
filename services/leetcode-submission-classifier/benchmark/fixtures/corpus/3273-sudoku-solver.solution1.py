# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sudoku-solver
# source_path: LeetCode-Solutions-master/Python/sudoku-solver.py
# solution_class: Solution
# submission_id: 48aa3624f490897ecf0c3dd088cf2fb9cb97052f
# seed: 1198442135

# Time:  ((9!)^9)
# Space: (1)

class Solution(object):
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def isValid(board, x, y):
            for i in xrange(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in xrange(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = 3 * (x / 3)
            while i < 3 * (x / 3 + 1):
                j = 3 * (y / 3)
                while j < 3 * (y / 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True

        def solver(board):
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in xrange(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)