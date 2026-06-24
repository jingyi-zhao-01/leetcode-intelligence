# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cells-with-odd-values-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/cells-with-odd-values-in-a-matrix.py
# solution_class: Solution
# submission_id: 90e8acd8b0aebfa08acd958ed1a5c53d784d2054
# seed: 2651273750

# Time:  O(n + m)
# Space: O(n + m)

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row, col = [0]*n, [0]*m
        for r, c in indices:
            row[r] ^= 1
            col[c] ^= 1
        row_sum, col_sum = sum(row), sum(col)
        return row_sum*m+col_sum*n-2*row_sum*col_sum