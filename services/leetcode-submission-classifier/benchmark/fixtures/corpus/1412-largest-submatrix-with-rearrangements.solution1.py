# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-submatrix-with-rearrangements
# source_path: LeetCode-Solutions-master/Python/largest-submatrix-with-rearrangements.py
# solution_class: Solution
# submission_id: 06148f8f84d718bfdfb71e8db962114fa33f7abd
# seed: 3908224939

# Time:  O(m * nlogn)
# Space: O(1)

class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for c in xrange(len(matrix[0])):
            h = 0
            for r in xrange(len(matrix)):
                h = h+1 if matrix[r][c] == 1 else 0
                matrix[r][c] = h
        result = 0
        for row in matrix:
            row.sort()
            for c in xrange(len(row)):
                result = max(result, (len(row)-c) * row[c])
        return result