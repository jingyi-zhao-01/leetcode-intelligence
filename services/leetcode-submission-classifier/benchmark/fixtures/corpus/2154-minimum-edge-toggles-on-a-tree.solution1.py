# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-edge-toggles-on-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-edge-toggles-on-a-tree.py
# solution_class: Solution
# submission_id: 7e2265fac68814ded067456a2058781dbe60874e
# seed: 1967802801

# Time:  O(n)
# Space: O(n)

# greedy, topological sort, bitmasks

class Solution(object):
    def minimumFlips(self, n, edges, start, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: str
        :type target: str
        :rtype: List[int]
        """
        diff = [1 if start[u] != target[u] else 0 for u in xrange(n)]
        if sum(diff)%2:
            return [-1]
        degree = [0]*n
        adj = [0]*n
        edge = [0]*n
        for idx, (u, v) in enumerate(edges):
            degree[u] += 1
            degree[v] += 1
            adj[u] ^= v
            adj[v] ^= u
            edge[u] ^= idx
            edge[v] ^= idx
        lookup = [False]*len(edges)
        for u in xrange(n):
            while degree[u] == 1:
                v, idx = adj[u], edge[u]
                degree[u] -= 1
                degree[v] -= 1
                adj[u] ^= v
                adj[v] ^= u
                edge[u] ^= idx
                edge[v] ^= idx
                if diff[u]:
                    diff[u] ^= 1
                    diff[v] ^= 1
                    lookup[idx] = True
                u = v
        return [i for i in xrange(len(lookup)) if lookup[i]]