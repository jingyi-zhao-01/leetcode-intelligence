# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: domino-and-tromino-tiling
# source_path: LeetCode-Solutions-master/Python/domino-and-tromino-tiling.py
# solution_class: Solution
# submission_id: 2733e4993ca0ea79e5702ae1ae48d0b272189ab5
# seed: 63428266

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        M = int(1e9+7)

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
            return [[sum(a*b for a, b in itertools.izip(row, col)) % M \
                     for col in ZB] for row in A]

        T = [[1, 0, 0, 1],  # #(|) = #(|) + #(=)
             [1, 0, 1, 0],  # #(「) = #(|) + #(L)
             [1, 1, 0, 0],  # #(L) = #(|) + #(「)
             [1, 1, 1, 0]]  # #(=) = #(|) + #(「) + #(L)

        return matrix_mult([[1, 0, 0, 0]], matrix_expo(T, N))[0][0] # [a0, a(-1), a(-2), a(-3)] * T^N