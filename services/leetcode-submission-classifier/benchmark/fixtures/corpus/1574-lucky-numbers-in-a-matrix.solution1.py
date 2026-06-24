# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lucky-numbers-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/lucky-numbers-in-a-matrix.py
# solution_class: Solution
# submission_id: 41618c2641d521062bac0450cf7bf691911c5583
# seed: 1543384142

# Time:  O(m * n)
# Space: O(m + n)

import itertools

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = map(min, matrix)
        cols = map(max, itertools.izip(*matrix))
        return [cell for i, row in enumerate(matrix)
                     for j, cell in enumerate(row) if rows[i] == cols[j]]