# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sparse-matrix-multiplication
# source_path: LeetCode-Solutions-master/Python/sparse-matrix-multiplication.py
# solution_class: Solution
# submission_id: 32f443f5ad17f7ba069ad9ef241a556afa122a60
# seed: 427804140

# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k]:
                    for j in xrange(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res