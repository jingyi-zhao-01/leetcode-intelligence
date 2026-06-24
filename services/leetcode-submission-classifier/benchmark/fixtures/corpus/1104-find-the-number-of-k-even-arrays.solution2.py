# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-k-even-arrays
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-k-even-arrays.py
# solution_class: Solution2
# submission_id: e688562fb8467c3bd1087b7afcbdb32774339f23
# seed: 304068046

# Time:  O(n)
# Space: O(n)

import collections


# stars and bars, combinatorics

class Solution2(object):
    def countOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        even, odd = m//2, (m+1)//2
        dp = [[0]*(k+1) for _ in xrange(2)]
        dp[0][0], dp[1][0] = even, odd
        for _ in xrange(n-1):
            for i in reversed(xrange(k+1)):
                dp[0][i], dp[1][i] = (((dp[0][i-1] if i-1 >= 0 else 0)+dp[1][i])*even)%MOD, ((dp[0][i]+dp[1][i])*odd)%MOD
        return (dp[0][k]+dp[1][k])%MOD