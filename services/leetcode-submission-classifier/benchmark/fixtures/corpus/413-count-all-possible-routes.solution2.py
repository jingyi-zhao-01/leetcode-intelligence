# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-all-possible-routes
# source_path: LeetCode-Solutions-master/Python/count-all-possible-routes.py
# solution_class: Solution2
# submission_id: 88df345112e4f417f768d24c68d9af0b41963a6f
# seed: 3541625288

# Time:  O(nlogn + n * f)
# Space: O(n * f)

import bisect

class Solution2(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0]*(fuel+1) for _ in xrange(len(locations))]
        dp[start][0] = 1
        for f in xrange(fuel+1):
            for i in xrange(len(locations)):
                for j in xrange(len(locations)):
                    if i == j:
                        continue
                    d = abs(locations[i]-locations[j])
                    if f-d < 0:
                        continue
                    dp[i][f] = (dp[i][f]+dp[j][f-d])%MOD
        return reduce(lambda x, y: (x+y)%MOD, dp[finish])