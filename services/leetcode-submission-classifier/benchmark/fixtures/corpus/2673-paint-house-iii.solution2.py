# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house-iii
# source_path: LeetCode-Solutions-master/Python/paint-house-iii.py
# solution_class: Solution2
# submission_id: 865c34af4c7d392e2eaef6f0adcc9aabb3470e41
# seed: 2431695965

# Time:  O(m * t * n^2)
# Space: O(t * n)

class Solution2(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = {(0, 0): 0}
        for i, p in enumerate(houses):
            new_dp = {}
            for nk in (xrange(1, n+1) if not p else [p]):
                for j, k in dp:
                    nj = j + (k != nk)
                    if nj > target:
                        continue
                    new_dp[nj, nk] = min(new_dp.get((nj, nk), float("inf")), dp[j, k] + (cost[i][nk-1] if nk != p else 0))
            dp = new_dp
        return min([dp[j, k] for j, k in dp if j == target] or [-1])