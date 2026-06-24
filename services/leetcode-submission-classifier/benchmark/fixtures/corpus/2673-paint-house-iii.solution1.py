# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house-iii
# source_path: LeetCode-Solutions-master/Python/paint-house-iii.py
# solution_class: Solution
# submission_id: 727bfc6c7fc779d2f6d9f44cceb991df15886043
# seed: 2692235471

# Time:  O(m * t * n^2)
# Space: O(t * n)

class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        # dp[i][j][k]: cost of covering i+1 houses with j+1 neighbor groups and the (k+1)th color
        dp = [[[float("inf") for _ in xrange(n)] for _ in xrange(target)] for _ in xrange(2)]
        for i in xrange(m):
            dp[i%2] = [[float("inf") for _ in xrange(n)] for _ in xrange(target)]
            for j in xrange(min(target, i+1)):
                for k in xrange(n):
                    if houses[i] and houses[i]-1 != k:
                        continue
                    same = dp[(i-1)%2][j][k] if i-1 >= 0 else 0
                    diff = (min([dp[(i-1)%2][j-1][nk] for nk in xrange(n) if nk != k] or [float("inf")]) if j-1 >= 0 else float("inf")) if i-1 >= 0 else 0
                    paint = cost[i][k] if not houses[i] else 0
                    dp[i%2][j][k] = min(same, diff)+paint
        result = min(dp[(m-1)%2][-1])
        return result if result != float("inf") else -1