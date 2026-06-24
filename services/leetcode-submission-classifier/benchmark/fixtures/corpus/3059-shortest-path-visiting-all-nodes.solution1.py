# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-path-visiting-all-nodes
# source_path: LeetCode-Solutions-master/Python/shortest-path-visiting-all-nodes.py
# solution_class: Solution
# submission_id: 3037bf49be35d1851508b20a1f1f8ffbc5c8b9a3
# seed: 963942700

# Time:  O(n * 2^n)
# Space: O(n * 2^n)

import collections

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        dp = [[float("inf")]*(len(graph))
              for _ in xrange(1 << len(graph))]
        q = collections.deque()
        for i in xrange(len(graph)):
            dp[1 << i][i] = 0
            q.append((1 << i, i))
        while q:
            state, node = q.popleft()
            steps = dp[state][node]
            for nei in graph[node]:
                new_state = state | (1 << nei)
                if dp[new_state][nei] == float("inf"):
                    dp[new_state][nei] = steps+1
                    q.append((new_state, nei))
        return min(dp[-1])