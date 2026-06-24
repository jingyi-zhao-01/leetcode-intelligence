# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-cost-of-trip-with-k-highways
# source_path: LeetCode-Solutions-master/Python/maximum-cost-of-trip-with-k-highways.py
# solution_class: Solution2
# submission_id: 65bed35cd20a4e32ed6fd72cd033c7d340d6ff22
# seed: 2036807286

# Time:  O(n^2 * 2^n)
# Space: O(n * 2^n)

import itertools


# combination based dp

class Solution2(object):
    def maximumCost(self, n, highways, k):
        """
        :type n: int
        :type highways: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k+1 > n:  # required to optimize, otherwise, TLE or MLE
            return -1
        adj = [[] for _ in xrange(n)]
        for c1, c2, t in highways:
            adj[c1].append((c2, t))
            adj[c2].append((c1, t))
        result = -1
        dp = [(u, 1<<u, 0) for u in xrange(n)]
        while dp:
            new_dp = []
            for u, mask, total in dp:
                if bin(mask).count('1') == k+1:
                    result = max(result, total)
                for v, t in adj[u]:
                    if mask&(1<<v) == 0:
                        new_dp.append((v, mask|(1<<v), total+t))
            dp = new_dp
        return result