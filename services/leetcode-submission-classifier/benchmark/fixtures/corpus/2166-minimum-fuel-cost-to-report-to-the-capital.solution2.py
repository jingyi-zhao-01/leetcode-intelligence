# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-fuel-cost-to-report-to-the-capital
# source_path: LeetCode-Solutions-master/Python/minimum-fuel-cost-to-report-to-the-capital.py
# solution_class: Solution
# submission_id: 9da3c6a18210d3452cdcf9b030249df04b28751a
# seed: 2582370608

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def dfs(u, p, d):
            cnt = 1+sum(dfs(v, u, d+1) for v in adj[u] if v != p)
            if d:
                result[0] += ceil_divide(cnt, seats)
            return cnt
    
        adj = [[] for _ in xrange(len(roads)+1)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1, 0)
        return result[0]