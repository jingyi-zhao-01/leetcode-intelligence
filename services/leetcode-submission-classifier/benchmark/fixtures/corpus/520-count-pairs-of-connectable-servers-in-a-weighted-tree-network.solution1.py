# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-connectable-servers-in-a-weighted-tree-network
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-connectable-servers-in-a-weighted-tree-network.py
# solution_class: Solution
# submission_id: ac5edd7a60cb1a897984d79444ac8f4090b03a25
# seed: 38660223

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        def iter_dfs(u, p, dist):
            result = 0
            stk = [(u, p, dist)]
            while stk:
                u, p, dist = stk.pop()
                if dist%signalSpeed == 0:
                    result += 1
                for v, w in reversed(adj[u]):
                    if v == p:
                        continue
                    stk.append((v, u, dist+w))
            return result
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in xrange(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = iter_dfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result