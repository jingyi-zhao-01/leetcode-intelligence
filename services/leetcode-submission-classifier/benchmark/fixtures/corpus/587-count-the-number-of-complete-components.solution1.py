# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-complete-components
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-complete-components.py
# solution_class: Solution
# submission_id: 77de7224dd4134359b086b06950143c8c4c645d7
# seed: 4104212802

# Time:  O(n)
# Space: O(n)

# bfs

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def bfs(u):
            if lookup[u]:
                return False
            v_cnt = e_cnt = 0
            lookup[u] = True
            q = [u]
            while q:
                new_q = []
                v_cnt += len(q)
                for u in q:
                    e_cnt += len(adj[u])
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return v_cnt*(v_cnt-1) == e_cnt

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [False]*n
        return sum(bfs(u) for u in xrange(n) if not lookup[u])