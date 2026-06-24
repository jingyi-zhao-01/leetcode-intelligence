# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fibonacci-number
# source_path: LeetCode-Solutions-master/Python/fibonacci-number.py
# solution_class: Solution
# submission_id: 2ac019b8d801bea1a4639f123818e13831129330
# seed: 2059417381

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution(object):
    def fib(self, N):
        """
        :type N: int
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
        return matrix_mult([[1, 0]], matrix_expo(T, N))[0][1]  # [a1, a0] * T^N