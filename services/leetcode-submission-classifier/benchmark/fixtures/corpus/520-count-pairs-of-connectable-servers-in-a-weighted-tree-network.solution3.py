# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-connectable-servers-in-a-weighted-tree-network
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-connectable-servers-in-a-weighted-tree-network.py
# solution_class: Solution3
# submission_id: 5e0e696c464cab64222834e34bf2300974dd504e
# seed: 1873573909

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution3(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        def bfs(u, p, dist):
            result = 0
            q = [(u, p, dist)]
            while q:
                new_q = []
                for u, p, dist in q:
                    if dist%signalSpeed == 0:
                        result += 1
                    for v, w in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u, dist+w))
                q = new_q
            return result
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in xrange(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = bfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result