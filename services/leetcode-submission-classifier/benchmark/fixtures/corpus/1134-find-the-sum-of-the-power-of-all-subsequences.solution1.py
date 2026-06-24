# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-sum-of-the-power-of-all-subsequences
# source_path: LeetCode-Solutions-master/Python/find-the-sum-of-the-power-of-all-subsequences.py
# solution_class: Solution
# submission_id: e7a389f0d8ba30bb59ebe102b5e3b83f40588195
# seed: 1667911747

# Time:  O(n * k)
# Space: O(k)

# dp, combinatorics

class Solution(object):
    def sumOfPower(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for x in nums:
            for i in reversed(xrange(k+1)):
                dp[i] = (dp[i]+(dp[i]+(dp[i-x] if i-x >= 0 else 0)))%MOD
        return dp[k]