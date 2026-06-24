# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-connectable-servers-in-a-weighted-tree-network
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-connectable-servers-in-a-weighted-tree-network.py
# solution_class: Solution2
# submission_id: e2b3193e4923c1b7202bec1544e6ea913a3539ac
# seed: 3323886945

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution2(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        def dfs(u, p, dist):
            cnt = 1 if dist%signalSpeed == 0 else 0
            for v, w in adj[u]:
                if v == p:
                    continue
                cnt += dfs(v, u, dist+w)
            return cnt
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in xrange(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = dfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result