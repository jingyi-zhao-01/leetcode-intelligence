# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: choose-edges-to-maximize-score-in-a-tree
# source_path: LeetCode-Solutions-master/Python/choose-edges-to-maximize-score-in-a-tree.py
# solution_class: Solution2
# submission_id: 5f7344169ba466814a0113c65c03466885ff34b0
# seed: 424071369

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution2(object):
    def maxScore(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(u):
            if not adj[u]:
                return (0, 0)
            children = [dfs(v) for v, _ in adj[u]]
            without_u = sum(max(with_v, without_v) for with_v, without_v in children)
            with_u = max(without_u-max(with_v, without_v)+(without_v+adj[u][i][1]) for i, (with_v, without_v) in enumerate(children))
            return (with_u, without_u)
            
        adj = [[] for _ in xrange(len(edges))]
        for i, (p, w) in enumerate(edges):
            if i == 0:
                continue
            adj[p].append((i, w))
        return max(dfs(0))