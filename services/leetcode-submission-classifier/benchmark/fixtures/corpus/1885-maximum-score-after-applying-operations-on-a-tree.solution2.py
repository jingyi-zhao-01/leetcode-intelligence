# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-after-applying-operations-on-a-tree
# source_path: LeetCode-Solutions-master/Python/maximum-score-after-applying-operations-on-a-tree.py
# solution_class: Solution2
# submission_id: c22bbbb7cd23b5434c593578017b1013d83cc536
# seed: 2760873692

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution2(object):
    def maximumScoreAfterOperations(self, edges, values):
        """
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        def dfs(u, p):
            if len(adj[u]) == (1 if u else 0):
                return values[u]
            return min(sum(dfs(v, u) for v in adj[u] if v != p), values[u])  # min(pick u, not pick u)

        adj = [[] for _ in xrange(len(values))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return sum(values)-dfs(0, -1)