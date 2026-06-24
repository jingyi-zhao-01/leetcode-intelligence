# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-number-of-target-nodes-after-connecting-trees-i
# source_path: LeetCode-Solutions-master/Python/maximize-the-number-of-target-nodes-after-connecting-trees-i.py
# solution_class: Solution3
# submission_id: 33202f187258527ec88bbf8ad724b1a984e4e6d6
# seed: 3827727811

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# dfs, centroid decomposition, prefix sum

class Solution3(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def bfs(u, adj, k):
            result = 0
            q = [(u, -1)]
            while q:
                if k == -1:
                    break
                k -= 1
                new_q = []
                result += len(q)
                for u, p in q:
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u))
                q = new_q
            return result
    
        def find_adj(edges):
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        adj2 = find_adj(edges2)
        mx = max(bfs(u, adj2, k-1) for u in xrange(len(adj2)))
        adj1 = find_adj(edges1)
        return [mx+bfs(u, adj1, k) for u in xrange(len(adj1))]