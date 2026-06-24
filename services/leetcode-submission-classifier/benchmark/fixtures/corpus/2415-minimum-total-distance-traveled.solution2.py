# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-total-distance-traveled
# source_path: LeetCode-Solutions-master/Python/minimum-total-distance-traveled.py
# solution_class: Solution2
# submission_id: 9d4f3f4367516b53076a3b2042fd928eb6f1a2ce
# seed: 4211857848

# Time:  O(mlogm + nlogn + m * n)
# Space: O(n)

import collections


# sort, dp, prefix sum, mono deque

class Solution2(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort(), factory.sort()
        dp = [float("inf")]*(len(robot)+1)  # dp[j] at i: min of factory[:i+1] and robot[:j]
        dp[0] = 0
        for i in xrange(len(factory)):
            for j in reversed(xrange(1, len(robot)+1)):
                curr = 0
                for k in xrange(min(factory[i][1], j)+1):
                    dp[j] = min(dp[j], dp[j-k]+curr)
                    if (j-1)-k >= 0:
                        curr += abs(robot[(j-1)-k]-factory[i][0])
        return dp[-1]