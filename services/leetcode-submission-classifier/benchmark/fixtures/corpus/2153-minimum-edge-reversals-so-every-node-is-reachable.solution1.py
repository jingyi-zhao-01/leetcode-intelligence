# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-edge-reversals-so-every-node-is-reachable
# source_path: LeetCode-Solutions-master/Python/minimum-edge-reversals-so-every-node-is-reachable.py
# solution_class: Solution
# submission_id: 02dee743d6197922fadb2bfd01d9b890e32666b5
# seed: 1358808325

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def iter_dfs1():
            result = 0
            stk = [(0, -1)]
            while stk:
                u, p = stk.pop()
                for v in adj[u].iterkeys():
                    if v == p:
                        continue
                    result += adj[u][v]
                    stk.append((v, u))
            return result

        def iter_dfs2(curr):
            result = [-1]*n
            stk = [(0, curr)]
            while stk:
                u, curr = stk.pop()
                result[u] = curr
                for v in adj[u].iterkeys():
                    if result[v] == -1:
                        stk.append((v, curr-adj[u][v]+adj[v][u]))
            return result
    
        adj = collections.defaultdict(dict)
        for u, v in edges:
            adj[u][v] = 0
            adj[v][u] = 1
        return iter_dfs2(iter_dfs1())