# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: climbing-stairs
# source_path: LeetCode-Solutions-master/Python/climbing-stairs.py
# solution_class: Solution
# submission_id: 21e1e25cb67c99c4b65a7a7bcea3a4203e79bb2b
# seed: 975035144

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def matrix_expo(A, K):
            result = [[int(i==j) for j in xrange(len(A))] \
                      for i in xrange(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b for a, b in itertools.izip(row, col)) \
                     for col in ZB] for row in A]

        T = [[1, 1],
             [1, 0]]
        return matrix_mult([[1,  0]], matrix_expo(T, n))[0][0]  # [a0, a(-1)] * T^n