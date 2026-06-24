# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-edge-toggles-on-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-edge-toggles-on-a-tree.py
# solution_class: Solution2
# submission_id: 70da3ee82351650bdd8c6ce4ae18e682a3c54871
# seed: 2974938683

# Time:  O(n)
# Space: O(n)

# greedy, topological sort, bitmasks

class Solution2(object):
    def minimumFlips(self, n, edges, start, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: str
        :type target: str
        :rtype: List[int]
        """
        def topological_sort():
            lookup = [False]*len(adj)
            q = [u for u in xrange(len(adj)) if degree[u] == 1]
            while q:
                new_q = []
                for u in q:
                    for v, idx in adj[u]:
                        if degree[v] == 0:
                            continue
                        degree[u] -= 1
                        degree[v] -= 1
                        if degree[v] == 1:
                            new_q.append(v)
                        if diff[u]:
                            diff[u] ^= 1
                            diff[v] ^= 1
                            lookup[idx] = True
                q = new_q
            return lookup

        diff = [1 if start[u] != target[u] else 0 for u in xrange(n)]
        if sum(diff)%2:
            return [-1]
        degree = [0]*n
        adj = [[] for _ in xrange(n)]
        for idx, (u, v) in enumerate(edges):
            degree[u] += 1
            degree[v] += 1
            adj[u].append((v, idx))
            adj[v].append((u, idx))
        lookup = topological_sort()
        return [i for i in xrange(len(lookup)) if lookup[i]]