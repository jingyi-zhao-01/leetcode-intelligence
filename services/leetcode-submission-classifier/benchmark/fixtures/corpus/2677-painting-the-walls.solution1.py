# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: painting-the-walls
# source_path: LeetCode-Solutions-master/Python/painting-the-walls.py
# solution_class: Solution
# submission_id: b9573ca7de21daad94ee49586f24183834ad31b4
# seed: 3794976403

# Time:  O(n^2)
# Space: O(n)

import itertools


# knapsack dp

class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        dp = [float("inf")]*(len(cost)+1)
        dp[0] = 0
        for c, t in itertools.izip(cost, time):
            for j in reversed(xrange(1, len(cost)+1)):
                dp[j] = min(dp[j], dp[max(j-(t+1), 0)]+c)
        return dp[-1]