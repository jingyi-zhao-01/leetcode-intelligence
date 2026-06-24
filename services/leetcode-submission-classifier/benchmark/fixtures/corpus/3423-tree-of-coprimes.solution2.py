# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tree-of-coprimes
# source_path: LeetCode-Solutions-master/Python/tree-of-coprimes.py
# solution_class: Solution2
# submission_id: a636234ca1e1591db3223ba4ea35c8d8cabdadec
# seed: 1756933259

# Time:  O(50 * n) = O(n)
# Space: O(n)

import collections
import fractions

class Solution2(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """        
        def dfs(nums, adj, prev, node, depth, path, result):
            max_d = -1
            for x in path.iterkeys():
                if fractions.gcd(nums[node], x) != 1:
                    continue
                if path[x][-1][1] > max_d:
                    max_d = path[x][-1][1]
                    result[node] = path[x][-1][0]
            path[nums[node]].append((node, depth))
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nums, adj, node, nei, depth+1, path, result)
            path[nums[node]].pop()
            if not path[nums[node]]:
                path.pop(nums[node])

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [-1]*len(nums)
        path = collections.defaultdict(list)
        dfs(nums, adj, -1, 0, 0, path, result)
        return result