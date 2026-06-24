# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-value-in-a-constrained-sequence
# source_path: LeetCode-Solutions-master/Python/find-maximum-value-in-a-constrained-sequence.py
# solution_class: Solution
# submission_id: add64bd720d5546d4f32c87d5eddf05685b359ea
# seed: 2213012733

# Time:  O(n)
# Space: O(n)

# greedy, dp

class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type diff: List[int]
        :rtype: int
        """
        dp = [float("inf")]*n
        dp[0] = 0
        for i, x in restrictions:
            dp[i] = x
        for i in xrange(n-1):
            dp[i+1] = min(dp[i+1], dp[i]+diff[i])
        for i in reversed(xrange(n-1)):
            dp[i] = min(dp[i], dp[i+1]+diff[i])
        return max(dp)