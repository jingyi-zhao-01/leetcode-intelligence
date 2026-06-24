# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-path-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/longest-increasing-path-in-a-matrix.py
# solution_class: Solution2
# submission_id: 8b8abe597b8304cdffe0aebdec79cac5e5774b69
# seed: 471897083

# Time:  O(m * n)
# Space: O(m * n)

# topological sort solution

class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]
            max_depth = 0
            for di, dj in directions:
                x, y = i+di, j+dj
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                   matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths))
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        if not matrix:
            return 0
        result = 0
        max_lengths = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                result = max(result, longestpath(matrix, i, j, max_lengths))
        return result