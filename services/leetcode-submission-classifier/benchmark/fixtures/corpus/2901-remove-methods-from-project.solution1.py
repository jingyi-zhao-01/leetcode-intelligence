# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-methods-from-project
# source_path: LeetCode-Solutions-master/Python/remove-methods-from-project.py
# solution_class: Solution
# submission_id: c2df5176e2dc50fa962451eccd8dc5b4bfb4bd93
# seed: 1114915908

# Time:  O(n + e)
# Space: O(n + e)

# bfs

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        def bfs():
            lookup = [False]*n
            lookup[k] = True
            q = [k]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return lookup

        adj = [[] for _ in xrange(n)]
        for u, v in invocations:
            adj[u].append(v)
        lookup = bfs()
        return [u for u in xrange(n) if not lookup[u]] if all(lookup[u] == lookup[v] for u, v in invocations) else range(n)