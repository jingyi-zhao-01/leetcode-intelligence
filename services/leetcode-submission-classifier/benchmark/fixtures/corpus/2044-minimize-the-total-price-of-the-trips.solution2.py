# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-total-price-of-the-trips
# source_path: LeetCode-Solutions-master/Python/minimize-the-total-price-of-the-trips.py
# solution_class: Solution2
# submission_id: 42957c4a387ae16360edf466993b4cd7d84783f8
# seed: 83380808

# Time:  O(t * n)
# Space: O(n)

# iterative dfs, tree dp

class Solution2(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        def dfs(u, p, target):
            lookup[u] += 1
            if u == target:
                return True
            for v in adj[u]:
                if v == p:
                    continue
                if dfs(v, u, target):
                    return True
            lookup[u] -= 1
            return False
    
        def dfs2(u, p):
            full, half = price[u]*lookup[u], price[u]//2*lookup[u]
            for v in adj[u]:
                if v == p:
                    continue
                f, h = dfs2(v, u)
                full += min(f, h)
                half += f
            return full, half

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*n
        for u, v in trips:
            dfs(u, -1, v)
        return min(dfs2(0, -1))