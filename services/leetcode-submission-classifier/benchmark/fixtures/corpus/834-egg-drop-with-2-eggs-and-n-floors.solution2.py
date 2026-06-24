# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: egg-drop-with-2-eggs-and-n-floors
# source_path: LeetCode-Solutions-master/Python/egg-drop-with-2-eggs-and-n-floors.py
# solution_class: Solution2
# submission_id: fa98d85aa28d2a9580c3dd053fb0b06c46b7902f
# seed: 795023067

# Time:  O(1)
# Space: O(1)

import math


# see the proof: https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/

class Solution2(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        K = 2
        dp = [[float("inf") for j in xrange(n+1)] for _ in xrange(2)]
        dp[1] = [j for j in xrange(n+1)]
        for i in xrange(2, K+1):
            dp[i%2][0] = 0
            for j in xrange(1, n+1):
                for k in xrange(1, j+1):
                    dp[i%2][j] = min(dp[i%2][j], 1+max(dp[(i-1)%2][k-1], dp[i%2][j-k]))
        return dp[K%2][n]