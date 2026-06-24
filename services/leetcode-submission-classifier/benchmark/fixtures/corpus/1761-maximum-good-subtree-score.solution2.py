# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-good-subtree-score
# source_path: LeetCode-Solutions-master/Python/maximum-good-subtree-score.py
# solution_class: Solution2
# submission_id: 78e72dfc40a2131943c1e833d9faa7e372170570
# seed: 2668191601

# Time:  O(n * (2^10)^2)
# Space: O(2^10)

import collections


# bitmasks, iterative dfs, tree dp

class Solution2(object):
    def goodSubtreeSum(self, vals, par):
        """
        :type vals: List[int]
        :type par: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        def get_mask(x):
            mask = 0
            while x:
                x, d = divmod(x, 10)
                if mask&(1<<d):
                    return -1
                mask |= 1<<d
            return mask

        def dfs(u):
            dp = collections.defaultdict(int)
            dp[0] = 0
            mask = get_mask(vals[u])
            if mask != -1:
                dp[mask] = vals[u]
            for v in adj[u]:
                new_dp = dfs(v)
                for m1, v1 in dp.items():
                    for m2, v2 in new_dp.iteritems():
                        if m1&m2:
                            continue
                        dp[m1|m2] =  max(dp[m1|m2], v1+v2)
            result[0] = (result[0]+max(dp.itervalues()))%MOD
            return dp

        adj = [[] for _ in xrange(len(vals))]
        for u in xrange(1, len(par)):
            adj[par[u]].append(u)
        result = [0]
        dfs(0)
        return result[0]