# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: inverse-coin-change
# source_path: LeetCode-Solutions-master/Python/inverse-coin-change.py
# solution_class: Solution2
# submission_id: bdf0e6a37f87159b099896d1f365c87d5af8674c
# seed: 3675485529

# Time:  O(n^2)
# Space: O(1)

# dp

class Solution2(object):
    def findCoins(self, numWays):
        """
        :type numWays: List[int]
        :rtype: List[int]
        """
        result = []
        dp = [0]*(len(numWays)+1)
        dp[0] = 1
        for i in xrange(1, len(numWays)+1):
            if numWays[i-1]-dp[i] == 1:
                result.append(i)
                for j in xrange(i, len(numWays)+1):
                    dp[j] += dp[j-i]
            if numWays[i-1]-dp[i]:
                return []
        return result