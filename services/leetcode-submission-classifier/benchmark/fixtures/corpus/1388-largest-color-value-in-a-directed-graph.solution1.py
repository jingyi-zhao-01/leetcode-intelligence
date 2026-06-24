# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-color-value-in-a-directed-graph
# source_path: LeetCode-Solutions-master/Python/largest-color-value-in-a-directed-graph.py
# solution_class: Solution
# submission_id: ec0b1833df7bf9e9ddfe6281369d4d6b694a4e9a
# seed: 1411072783

# Time:  O(n + m)
# Space: O(n + m)

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in xrange(len(colors))]
        in_degree = [0]*len(colors)
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        q = []
        for u in xrange(len(colors)):
            if not in_degree[u]:
                q.append(u)
        dp = [[0]*26 for _ in xrange(len(colors))]
        result, cnt = -1, 0
        while q:
            new_q = []
            for u in q:
                cnt += 1
                dp[u][ord(colors[u])-ord('a')] += 1
                result = max(result, dp[u][ord(colors[u])-ord('a')])
                for v in adj[u]:
                    for c in xrange(26):
                        dp[v][c] = max(dp[v][c], dp[u][c])
                    in_degree[v] -= 1
                    if not in_degree[v]:
                        new_q.append(v)
            q = new_q
        return result if cnt == len(colors) else -1