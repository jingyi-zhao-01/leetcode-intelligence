# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-number-of-target-nodes-after-connecting-trees-i
# source_path: LeetCode-Solutions-master/Python/maximize-the-number-of-target-nodes-after-connecting-trees-i.py
# solution_class: Solution2
# submission_id: 7751c307ac03b5706c3280cb67fa71ab2457ce97
# seed: 2534950394

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# dfs, centroid decomposition, prefix sum

class Solution2(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def tree_dp(adj, k):
            def dfs1(u, p):
                for v in adj[u]:
                    if v == p:
                        continue
                    dfs1(v, u)
                dp[u][0] += 1
                for v in adj[u]:
                    if v == p:
                        continue
                    for d in xrange(k):
                        dp[u][d+1] += dp[v][d]
            
            def dfs2(u, p, curr):
                def update(v, u, curr):
                    new_curr = [0]*len(curr)
                    for d in xrange(len(curr)-1):
                        new_curr[d+1] = curr[d]+(dp[u][d]-(dp[v][d-1] if d-1 >= 0 else 0))
                    return new_curr

                for v in adj[u]:
                    if v == p:
                        continue
                    dfs2(v, u, update(v, u, curr))
                result[u] = sum(dp[u][i]+curr[i] for i in xrange(len(curr)))

            result = [0]*len(adj)
            k = min(k, len(adj)-1)
            if k == -1:
                return result
            dp = [[0]*(k+1) for _ in xrange(len(adj))]
            dfs1(0, -1)
            dfs2(0, -1, [0]*(k+1))
            return result

        def find_adj(edges):
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adj2 = find_adj(edges2)
        mx = max(tree_dp(adj2, k-1))
        adj1 = find_adj(edges1)
        return [mx+x for x in tree_dp(adj1, k)]