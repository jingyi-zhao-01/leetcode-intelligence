# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-tourist-can-earn
# source_path: LeetCode-Solutions-master/Python/maximum-points-tourist-can-earn.py
# solution_class: Solution
# submission_id: 94a8904ef600e08f55ffb8c34094a5702355ad38
# seed: 3053568212

# Time:  O(k * n^2)
# Space: O(n)

# dp

class Solution(object):
    def maxScore(self, n, k, stayScore, travelScore):
        """
        :type n: int
        :type k: int
        :type stayScore: List[List[int]]
        :type travelScore: List[List[int]]
        :rtype: int
        """
        dp = [0]*n
        for i in xrange(k):
            dp = [max(dp[u]+stayScore[i][u], max(dp[v]+travelScore[v][u] for v in xrange(n))) for u in xrange(n)]
        return max(dp)