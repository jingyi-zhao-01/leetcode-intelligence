# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-sudoku
# source_path: LeetCode-Solutions-master/Python/valid-sudoku.py
# solution_class: Solution
# submission_id: b7b16b9e624168cf36e17a8698ee808c6fe60cdf
# seed: 3889449815

# Time:  O(9^2)
# Space: O(9)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
               not self.isValidList([board[j][i] for j in xrange(9)]):
                return False
        for i in xrange(3):
            for j in xrange(3):
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                                     for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList(self, xs):
        xs = filter(lambda x: x != '.', xs)
        return len(set(xs)) == len(xs)