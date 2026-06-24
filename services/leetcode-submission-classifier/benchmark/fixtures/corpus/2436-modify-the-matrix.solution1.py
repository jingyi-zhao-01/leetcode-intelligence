# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: modify-the-matrix
# source_path: LeetCode-Solutions-master/Python/modify-the-matrix.py
# solution_class: Solution
# submission_id: 072bda4e683d9c588f1c52776dd3a7aa2fb5f2df
# seed: 1900886172

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        for j in xrange(len(matrix[0])):
            mx = max(matrix[i][j] for i in xrange(len(matrix)))
            for i in xrange(len(matrix)):
                if matrix[i][j] == -1:
                    matrix[i][j] = mx
        return matrix