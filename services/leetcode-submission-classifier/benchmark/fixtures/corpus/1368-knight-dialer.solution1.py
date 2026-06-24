# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: knight-dialer
# source_path: LeetCode-Solutions-master/Python/knight-dialer.py
# solution_class: Solution
# submission_id: e0cd3f7a5e1987963ff6ec3c348b962ec1640596
# seed: 4054515116

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution(object):
    def knightDialer(self, N):
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
            return [[sum(a*b for a, b in itertools.izip(row, col)) % M \
                     for col in ZB] for row in A]
        
        M = 10**9 + 7
        T = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
        return sum(map(sum, matrix_expo(T, N-1))) % M