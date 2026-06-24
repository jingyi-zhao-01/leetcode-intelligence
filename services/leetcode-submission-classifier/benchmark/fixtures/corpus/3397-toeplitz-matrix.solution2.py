# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: toeplitz-matrix
# source_path: LeetCode-Solutions-master/Python/toeplitz-matrix.py
# solution_class: Solution2
# submission_id: 8d07b1b4c4d4bfc910ee6e258268cd4bc150eee8
# seed: 1291878286

# Time:  O(m * n)
# Space: O(1)

class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row_index, row in enumerate(matrix):
            for digit_index, digit in enumerate(row):
                if not row_index or not digit_index:
                    continue
                if matrix[row_index - 1][digit_index - 1] != digit:
                    return False
        return True