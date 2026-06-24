# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-after-collecting-coins-from-all-nodes
# source_path: LeetCode-Solutions-master/Python/maximum-points-after-collecting-coins-from-all-nodes.py
# solution_class: Solution2
# submission_id: 35cb1ce0632b62a02a6525c1c1907c036858f2a6
# seed: 4286843019

# Time:  O(nlogr), r = max(coins)
# Space: O(n)

# dfs, bitmasks, pruning

class Solution2(object):
    def maximumPoints(self, edges, coins, k):
        """
        :type edges: List[List[int]]
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def memoization(u, p, d):
            if d >= max_d:
                return 0
            if lookup[u][d] is None:
                lookup[u][d] = max(((coins[u]>>d)-k)+sum(memoization(v, u, d) for v in adj[u] if v != p),
                                    (coins[u]>>(d+1))+sum(memoization(v, u, d+1) for v in adj[u] if v != p))
            return lookup[u][d]

        adj = [[] for _ in xrange(len(coins))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        max_d = max(coins).bit_length()
        lookup = [[None]*max_d for _ in xrange(len(coins))]
        return memoization(0, -1, 0)