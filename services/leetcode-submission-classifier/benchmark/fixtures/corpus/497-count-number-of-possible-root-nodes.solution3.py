# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-possible-root-nodes
# source_path: LeetCode-Solutions-master/Python/count-number-of-possible-root-nodes.py
# solution_class: Solution3
# submission_id: 9dde293571e003d8e21fcc771c5d42f51f6068f3
# seed: 2441199301

# Time:  O(n) 
# Space: O(h)

import collections


# iterative dfs

class Solution3(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        cnt = [0]
        def memoization(u, p):
            if (u, p) not in memo:
                memo[u, p] = int((p, u) in lookup)
                for v in adj[u]:
                    if v == p:
                        continue
                    cnt[0] += 1
                    memo[u, p] += memoization(v, u)
            return memo[u, p]

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        memo = {}
        return sum(memoization(i, -1) >= k for i in adj.iterkeys())