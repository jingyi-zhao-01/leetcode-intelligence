# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-ways-to-choose-coprime-integers-from-rows
# source_path: LeetCode-Solutions-master/Python/count-ways-to-choose-coprime-integers-from-rows.py
# solution_class: Solution2
# submission_id: 5e7e3749afe2d5ef0cddb7f602bd28b5fe5e5b8f
# seed: 3978455582

# Time:  O(n * (m + rlogr)), r = max(max(row) for row in mat)
# Space: O(r)

import collections


# dp, number theory, mobius function, principle of inclusion-exclusion, freq table

class Solution2(object):
    def countCoprime(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        dp = collections.defaultdict(int)
        dp[0] = 1
        for row in mat:
            new_dp = collections.defaultdict(int)
            for x in row:
                for g, c in dp.iteritems():
                    ng = gcd(g, x)
                    new_dp[ng] = (new_dp[ng]+c)%MOD
            dp = new_dp
        return dp[1]