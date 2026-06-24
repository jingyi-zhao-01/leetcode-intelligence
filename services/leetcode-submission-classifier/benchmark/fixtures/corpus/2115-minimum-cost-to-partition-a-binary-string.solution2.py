# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-partition-a-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-partition-a-binary-string.py
# solution_class: Solution2
# submission_id: 75ac060459d14bedeea7fd073be32995ae008292
# seed: 1290226089

# Time:  O(n)
# Space: O(n)

# prefix sum, divide and conquer

class Solution2(object):
    def minCost(self, s, encCost, flatCost):
        """
        :type s: str
        :type encCost: int
        :type flatCost: int
        :rtype: int
        """
        l = len(s)
        while l%2 == 0:
            l //= 2
        result = 0
        dp = []
        for left in xrange(0, len(s), l):
            x = sum(s[i] == '1' for i in xrange(left, left+l))
            dp.append((l*x*encCost if x else flatCost, x))
        while len(dp) != 1:
            new_dp = []
            l *= 2
            for i in xrange(0, len(dp), 2):
                v = dp[i][0]+dp[i+1][0]
                x = dp[i][1]+dp[i+1][1]
                new_dp.append(((min(l*x*encCost, v) if x else flatCost), x))
            dp = new_dp
        return dp[0][0]