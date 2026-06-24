# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-a-2d-matrix-ii
# source_path: LeetCode-Solutions-master/Python/search-a-2d-matrix-ii.py
# solution_class: Solution
# submission_id: da80b4f417ff637699578a632c078920413b6a31
# seed: 3346039649

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False