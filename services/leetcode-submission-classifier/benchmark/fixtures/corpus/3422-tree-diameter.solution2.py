# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tree-diameter
# source_path: LeetCode-Solutions-master/Python/tree-diameter.py
# solution_class: Solution2
# submission_id: 192d39131cf4a2b57a4eab5dfb3512ef90a27ff8
# seed: 2500160512

# Time:  O(|V| + |E|)
# Space: O(|E|)

# iterative dfs

class Solution2(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(u, p):
            mx = 0
            for v in adj[u]:
                if v == p:
                    continue
                curr = dfs(v, u)
                result[0] = max(result[0], mx+(curr+1))
                mx = max(mx, curr+1)
            return mx
            
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]