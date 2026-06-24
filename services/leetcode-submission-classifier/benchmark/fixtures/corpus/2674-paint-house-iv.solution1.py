# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house-iv
# source_path: LeetCode-Solutions-master/Python/paint-house-iv.py
# solution_class: Solution
# submission_id: cbacc610a3662b3984c4b9d4565de5d7dbb069ef
# seed: 1388421481

# Time:  O(n * l^4)
# Space: O(l^2)

# dp

class Solution(object):
    def minCost(self, n, cost):
        """
        :type n: int
        :type cost: List[List[int]]
        :rtype: int
        """
        l = len(cost[0])
        dp = [[0]*l for i in xrange(l)]
        for k in xrange(n//2):
            new_dp = [[float("inf")]*l for i in xrange(l)]
            for i in xrange(l):
                for j in xrange(l):
                    if j == i:
                        continue
                    for ni in xrange(l):
                        if ni == i:
                            continue
                        for nj in xrange(l):
                            if nj == j or ni == nj:
                                continue
                            new_dp[ni][nj] = min(new_dp[ni][nj], dp[i][j]+cost[k][ni]+cost[~k][nj])
            dp = new_dp
        return min(dp[i][j] for i in xrange(l) for j in xrange(l) if i != j)