# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-cut-a-stick
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-cut-a-stick.py
# solution_class: Solution
# submission_id: 8f9163554d86319b99afe3088d9571d147919263
# seed: 743103293

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        sorted_cuts = sorted(cuts + [0, n])
        dp = [[0]*len(sorted_cuts) for _ in xrange(len(sorted_cuts))]
        for l in xrange(2, len(sorted_cuts)):
            for i in xrange(len(sorted_cuts)-l):
                dp[i][i+l] = min(dp[i][j]+dp[j][i+l] for j in xrange(i+1, i+l)) + \
                             sorted_cuts[i+l]-sorted_cuts[i]
        return dp[0][len(sorted_cuts)-1]