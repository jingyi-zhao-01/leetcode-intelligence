# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: handshakes-that-dont-cross
# source_path: LeetCode-Solutions-master/Python/handshakes-that-dont-cross.py
# solution_class: Solution
# submission_id: 4464d0c2464df8287e36061a03e4dfe702c37b95
# seed: 2215693250

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        MOD = 10**9+7
        def inv(x, m):  # Euler's Theorem
            return pow(x, m-2, m)  # O(logMOD) = O(1)

        def nCr(n, k, m):
            if n-k < k:
                return nCr(n, n-k, m)
            result = 1
            for i in xrange(1, k+1):
                result = result*(n-k+i)*inv(i, m)%m
            return result

        n = num_people//2
        return nCr(2*n, n, MOD)*inv(n+1, MOD) % MOD  # Catalan number