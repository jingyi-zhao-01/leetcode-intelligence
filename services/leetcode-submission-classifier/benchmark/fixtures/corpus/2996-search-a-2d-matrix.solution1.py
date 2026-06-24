# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-a-2d-matrix
# source_path: LeetCode-Solutions-master/Python/search-a-2d-matrix.py
# solution_class: Solution
# submission_id: 395905e4b2bd863814b5e47a6ec2d21acf1a435b
# seed: 3985413573

# Time:  O(logm + logn)
# Space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) / 2
            if matrix[mid / n][mid % n] >= target:
                right = mid
            else:
                left = mid + 1

        return left < m * n and matrix[left / n][left % n] == target