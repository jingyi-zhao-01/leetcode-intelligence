# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-number-of-coins-to-place-in-tree-nodes
# source_path: LeetCode-Solutions-master/Python/find-number-of-coins-to-place-in-tree-nodes.py
# solution_class: Solution2
# submission_id: 92f4299e990a650df949f2f94c44b40a0fa3b40b
# seed: 3611456756

# Time:  O(n)
# Space: O(n)

# iterative dfs

class Solution2(object):
    def placedCoins(self, edges, cost):
        """
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: List[int]
        """
        def dfs(u, p):
            arr = [cost[u]]
            for v in adj[u]:
                if v == p:
                    continue
                arr.extend(dfs(v, u))
                arr.sort()
                if len(arr) > 5:
                    arr = arr[:2]+arr[-3:]
            result[u] = 1 if len(arr) < 3 else max(arr[0]*arr[1]*arr[-1], arr[-3]*arr[-2]*arr[-1], 0)
            return arr
                
        adj = [[] for _ in xrange(len(cost))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]*len(cost)
        dfs(0, -1)
        return result