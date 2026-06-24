# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-profitable-path-in-a-tree
# source_path: LeetCode-Solutions-master/Python/most-profitable-path-in-a-tree.py
# solution_class: Solution2
# submission_id: 5f222d6603916057807423edaed61218970a164b
# seed: 1702321604

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution2(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        def dfs(u, ah):
            lookup[u] = True
            result = 0 if len(adj[u])+(u == 0) == 1 else float("-inf")
            bh = 0 if u == bob else float("inf")
            for v in adj[u]:
                if lookup[v]:
                    continue
                r, h = dfs(v, ah+1)
                result = max(result, r)
                bh = min(bh, h)
            if ah == bh:
                result += amount[u]//2
            elif ah < bh:
                result += amount[u]
            return result, bh+1

        adj = [[] for _ in xrange(len(edges)+1)]
        lookup = [False]*len(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return dfs(0, 0)[0]