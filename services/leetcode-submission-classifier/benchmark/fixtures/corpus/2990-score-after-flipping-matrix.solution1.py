# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: score-after-flipping-matrix
# source_path: LeetCode-Solutions-master/Python/score-after-flipping-matrix.py
# solution_class: Solution
# submission_id: 5cd94a35b4e4400b037e32b6bcd393f5ac95099c
# seed: 1257895073

# Time:  O(r * c)
# Space: O(1)

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        result = 0
        for c in xrange(C):
            col = 0
            for r in xrange(R):
                col += A[r][c] ^ A[r][0]
            result += max(col, R-col) * 2**(C-1-c)
        return result