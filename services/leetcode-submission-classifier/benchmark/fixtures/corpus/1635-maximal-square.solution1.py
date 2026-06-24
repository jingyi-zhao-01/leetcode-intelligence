# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-square
# source_path: LeetCode-Solutions-master/Python/maximal-square.py
# solution_class: Solution
# submission_id: ead5fff6bb48049ac54a66da2133a37640cc4bfe
# seed: 4255199883

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(2)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i % 2][0] = 1
            else:
                size[i % 2][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[i % 2][j - 1], \
                                         size[(i - 1) % 2][j], \
                                         size[(i - 1) % 2][j - 1]) + 1
                    max_size = max(max_size, size[i % 2][j])
                else:
                    size[i % 2][j] = 0

        return max_size * max_size