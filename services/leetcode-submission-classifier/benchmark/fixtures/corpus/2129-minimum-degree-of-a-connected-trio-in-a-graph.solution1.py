# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-degree-of-a-connected-trio-in-a-graph
# source_path: LeetCode-Solutions-master/Python/minimum-degree-of-a-connected-trio-in-a-graph.py
# solution_class: Solution
# submission_id: ad76297e636ac641a7af49a25ffbab0808a88e74
# seed: 2432806170

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in xrange(n+1)]
        degree = [0]*(n+1)
        for u, v in edges:
            adj[min(u, v)].add(max(u, v))
            degree[u] += 1
            degree[v] += 1
        result = float("inf")
        for u in xrange(1, n+1):
            for v in adj[u]:
                for w in adj[u]:
                    if v < w and w in adj[v]:
                        result = min(result, degree[u]+degree[v]+degree[w] - 6)
        return result if result != float("inf") else -1