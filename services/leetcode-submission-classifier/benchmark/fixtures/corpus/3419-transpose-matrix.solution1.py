# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transpose-matrix
# source_path: LeetCode-Solutions-master/Python/transpose-matrix.py
# solution_class: Solution
# submission_id: 9175cb9b9faadc113c4b1354fc70fdcf80908223
# seed: 3157420717

# Time:  O(r * c)
# Space: O(1)

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[None] * len(A) for _ in xrange(len(A[0]))]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                result[c][r] = val
        return result