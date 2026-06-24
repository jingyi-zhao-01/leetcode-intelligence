# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-most-similar-path-in-a-graph
# source_path: LeetCode-Solutions-master/Python/the-most-similar-path-in-a-graph.py
# solution_class: Solution
# submission_id: c925c8b3419d528aac1010eb835f10715cbb7e31
# seed: 1344893397

# Time:  O(n^2 * m), m is the length of targetPath
# Space: O(n * m)

class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        adj = [[] for _ in xrange(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        dp = [[0]*n for _ in xrange(len(targetPath)+1)]
        for i in xrange(1, len(targetPath)+1):
            for v in xrange(n):
                dp[i][v] = (names[v] != targetPath[i-1]) + min(dp[i-1][u] for u in adj[v]) 

        path = [dp[-1].index(min(dp[-1]))]
        for i in reversed(xrange(2, len(targetPath)+1)):
            for u in adj[path[-1]]:
                if dp[i-1][u]+(names[path[-1]] != targetPath[i-1]) == dp[i][path[-1]]:
                    path.append(u)
                    break
        return path[::-1]