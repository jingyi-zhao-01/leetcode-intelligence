# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diagonal-traverse
# source_path: LeetCode-Solutions-master/Python/diagonal-traverse.py
# solution_class: Solution
# submission_id: da28be7f5718fc216c27e8bc81d1829342208132
# seed: 2806955482

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        row, col, d = 0, 0, 0
        dirs = [(-1, 1), (1, -1)]

        for i in xrange(len(matrix) * len(matrix[0])):
            result.append(matrix[row][col])
            row += dirs[d][0]
            col += dirs[d][1]

            if row >= len(matrix):
                row = len(matrix) - 1
                col += 2
                d = 1 - d
            elif col >= len(matrix[0]):
                col = len(matrix[0]) - 1
                row += 2
                d = 1 - d
            elif row < 0:
                row = 0
                d = 1 - d
            elif col < 0:
                col = 0
                d = 1 - d

        return result