# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: profitable-schemes
# source_path: LeetCode-Solutions-master/Python/profitable-schemes.py
# solution_class: Solution
# submission_id: ae30ef5c076a205cb8f24f6c0220cf2d8152ac8d
# seed: 295909231

# Time:  O(n * p * g)
# Space: O(p * g)

import itertools

class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0 for _ in xrange(G+1)] for _ in xrange(P+1)]
        dp[0][0] = 1
        for p, g in itertools.izip(profit, group):
            for i in reversed(xrange(P+1)):
                for j in reversed(xrange(G-g+1)):
                    dp[min(i+p, P)][j+g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)