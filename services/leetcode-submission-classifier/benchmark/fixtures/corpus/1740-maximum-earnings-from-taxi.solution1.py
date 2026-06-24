# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-earnings-from-taxi
# source_path: LeetCode-Solutions-master/Python/maximum-earnings-from-taxi.py
# solution_class: Solution
# submission_id: bc6d369e7768b85e8fe8bb7345f2b50ea749eed7
# seed: 3285574595

# Time:  O(n + mlogm), m is the number of rides
# Space: O(n)

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides.sort()
        dp = [0]*(n+1)
        j = 0
        for i in xrange(1, n+1):
            dp[i] = max(dp[i], dp[i-1])
            while j < len(rides) and rides[j][0] == i:
                dp[rides[j][1]] = max(dp[rides[j][1]], dp[i]+rides[j][1]-rides[j][0]+rides[j][2])
                j += 1
        return dp[-1]