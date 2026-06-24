# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-image
# source_path: LeetCode-Solutions-master/Python/rotate-image.py
# solution_class: Solution
# submission_id: 0ed7a43ad618caf5b31690b89a3c6a471a6d7712
# seed: 701335517

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        # anti-diagonal mirror
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        # horizontal mirror
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix