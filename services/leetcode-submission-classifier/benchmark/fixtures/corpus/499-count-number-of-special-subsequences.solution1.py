# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-special-subsequences
# source_path: LeetCode-Solutions-master/Python/count-number-of-special-subsequences.py
# solution_class: Solution
# submission_id: 143c9004fd463ce6fc3c9495333fed0f886408cf
# seed: 802826789

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*3
        for x in nums:
            dp[x] = ((dp[x]+dp[x])%MOD+(dp[x-1] if x-1 >= 0 else 1))%MOD
        return dp[-1]