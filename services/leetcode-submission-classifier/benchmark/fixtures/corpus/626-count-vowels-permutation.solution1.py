# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-vowels-permutation
# source_path: LeetCode-Solutions-master/Python/count-vowels-permutation.py
# solution_class: Solution
# submission_id: 2fa0cdfb2ba81f4e55bbf3102e548fcad157b6ae
# seed: 2289014162

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution(object):
    def countVowelPermutation(self, n):
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
            return [[sum(a*b for a, b in itertools.izip(row, col)) % MOD \
                     for col in ZB] for row in A]
        
        MOD = 10**9 + 7
        T = [[0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 1, 0]]
        return sum(map(sum, matrix_expo(T, n-1))) % MOD