# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: toeplitz-matrix
# source_path: LeetCode-Solutions-master/Python/toeplitz-matrix.py
# solution_class: Solution
# submission_id: 124fdbc62a7112c154ea40e3550f51f27f54c448
# seed: 3444333396

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(i == 0 or j == 0 or matrix[i-1][j-1] == val
                   for i, row in enumerate(matrix)
                   for j, val in enumerate(row))