# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-good-subtree-score
# source_path: LeetCode-Solutions-master/Python/maximum-good-subtree-score.py
# solution_class: Solution
# submission_id: 52b44d6903705c0a304ae7e14cb22596055d17a4
# seed: 2208003514

# Time:  O(n * (2^10)^2)
# Space: O(2^10)

import collections


# bitmasks, iterative dfs, tree dp

class Solution(object):
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

        def iter_dfs():
            result = 0
            ret = collections.defaultdict(int)
            stk = [(1, (0, ret))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, ret = args
                    ret[0] = 0
                    mask = get_mask(vals[u])
                    if mask != -1:
                        ret[mask] = vals[u]
                    stk.append((4, (u, ret)))
                    stk.append((2, (u, 0, ret)))
                elif step == 2:
                    u, i, ret = args
                    if i == len(adj[u]):
                        continue
                    v = adj[u][i]
                    stk.append((2, (u, i+1, ret)))
                    new_ret = collections.defaultdict(int)
                    stk.append((3, (new_ret, ret)))
                    stk.append((1, (v, new_ret)))
                elif step == 3:
                    new_ret, ret = args
                    for m1, v1 in ret.items():
                        for m2, v2 in new_ret.iteritems():
                            if m1&m2:
                                continue
                            ret[m1|m2] =  max(ret[m1|m2], v1+v2)
                elif step == 4:
                    u, ret = args
                    result = (result+max(ret.itervalues()))%MOD
            return result

        adj = [[] for _ in xrange(len(vals))]
        for u in xrange(1, len(par)):
            adj[par[u]].append(u)
        return iter_dfs()