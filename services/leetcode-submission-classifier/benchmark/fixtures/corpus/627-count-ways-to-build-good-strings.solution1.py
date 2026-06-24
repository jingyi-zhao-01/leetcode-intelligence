# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-ways-to-build-good-strings
# source_path: LeetCode-Solutions-master/Python/count-ways-to-build-good-strings.py
# solution_class: Solution
# submission_id: c0e3daf03bad54d5518982073d2145c947eb63cc
# seed: 2316836798

# Time:  O(n)
# Space: O(n)

# dp

class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        dp = [0]*(high+1)
        dp[0] = 1
        for i in xrange(1, high+1):
            if i >= zero:
                dp[i] = (dp[i]+dp[i-zero])%MOD
            if i >= one:
                dp[i] = (dp[i]+dp[i-one])%MOD
            if i >= low:
                result = (result+dp[i])%MOD
        return result