# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-value-of-covered-indices
# source_path: LeetCode-Solutions-master/Python/maximum-total-value-of-covered-indices.py
# solution_class: Solution2
# submission_id: 23551c1132730416f9b49457140ae2d4b1fcfbe7
# seed: 1379790320

# Time:  O(n)
# Space: O(1)

# greedy

class Solution2(object):
    def maxTotal(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        NEG_INF = float("-inf")
        dp = [NEG_INF]*2
        dp[0] = 0
        for i in xrange(len(s)):
            new_dp = [NEG_INF]*2
            if s[i] == '0':
                new_dp[0] = max(dp)
            else:
                new_dp[1] = max(dp)+nums[i]
                if i-1 >= 0:
                    new_dp[0] = dp[0]+nums[i-1]
            dp = new_dp
        return max(dp)