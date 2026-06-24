# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: choose-edges-to-maximize-score-in-a-tree
# source_path: LeetCode-Solutions-master/Python/choose-edges-to-maximize-score-in-a-tree.py
# solution_class: Solution
# submission_id: 8111e52bf68bab2ab7b54367206601f871c0096b
# seed: 2878437324

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution(object):
    def maxScore(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def iter_dfs():
            result = [(0, 0) for _ in xrange(len(adj))]
            stk = [(1, 0)]
            while stk:
                step, u = stk.pop()
                if step == 1:
                    if not adj[u]:
                        continue
                    stk.append((2, u))
                    for v, _ in adj[u]:
                        stk.append((1, v))
                elif step == 2:
                    without_u = sum(max(result[v]) for v, w in adj[u])
                    with_u = max(without_u-max(result[v])+(result[v][1]+w) for v, w in adj[u])
                    result[u] = (with_u, without_u)
            return max(result[0])
            
        adj = [[] for _ in xrange(len(edges))]
        for i, (p, w) in enumerate(edges):
            if i == 0:
                continue
            adj[p].append((i, w))
        return iter_dfs()