# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-ways-to-place-houses
# source_path: LeetCode-Solutions-master/Python/count-number-of-ways-to-place-houses.py
# solution_class: Solution
# submission_id: 4fea19eb970e9b07ee48f08343fb22860c7fc98a
# seed: 3206537309

# Time:  O(logn)
# Space: O(1)

import itertools


# matrix exponentiation

class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b % MOD for a, b in itertools.izip(row, col)) % MOD for col in ZB] for row in A]
 
        def matrix_expo(A, K):
            result = [[int(i == j) for j in xrange(len(A))] for i in xrange(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        T = [[1, 1],
             [1, 0]]
        return pow(matrix_mult([[2, 1]], matrix_expo(T, n-1))[0][0], 2, MOD)  # [a1, a0] * T^(n-1) = [an, a(n-1)]