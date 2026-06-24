# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-number-of-target-nodes-after-connecting-trees-i
# source_path: LeetCode-Solutions-master/Python/maximize-the-number-of-target-nodes-after-connecting-trees-i.py
# solution_class: Solution
# submission_id: 42a92dab1aea23bb32fc2d8d1f682bf59b0c8fc4
# seed: 2068994461

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# dfs, centroid decomposition, prefix sum

class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def centroid_decomposition(adj, k):
            def dfs(u):
                # https://usaco.guide/plat/centroid
                def find_subtree_size(u, p):
                    sizes[u] = 1
                    for v in adj[u]:
                        if v == p or lookup[v]:
                            continue
                        sizes[u] += find_subtree_size(v, u)
                    return sizes[u]

                def find_centroid(u, p):
                    for v in adj[u]:
                        if v == p or lookup[v]:
                            continue
                        if sizes[v]*2 > n:
                            return find_centroid(v, u)
                    return u

                def count(u, p, d):
                    if d > k:
                        return
                    if d-1 == len(cnt):
                        cnt.append(0)
                    cnt[d-1] += 1
                    for v in adj[u]:
                        if v == p or lookup[v]:
                            continue
                        count(v, u, d+1)

                def update(u, p, d):
                    if d > k:
                        return
                    result[u] += total[min(k-d, len(total)-1)]-curr[min(k-d, len(curr)-1)]
                    for v in adj[u]:
                        if v == p or lookup[v]:
                            continue
                        update(v, u, d+1)

                find_subtree_size(u, -1)
                n = sizes[u]
                u = find_centroid(u, -1)
                lookup[u] = True
                max_d = 0
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    cnt = []
                    count(v, u, 0+1)
                    prefix[v].append(0)
                    for d in xrange(len(cnt)):
                        prefix[v].append(prefix[v][-1]+cnt[d])
                    max_d = max(max_d, len(cnt))
                total = [1]*(max_d+1)
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    for d in xrange(len(total)):
                        total[d] += prefix[v][min(d, len(prefix[v])-1)]
                result[u] += total[min(k, len(total)-1)]
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    curr, prefix[v] = prefix[v], []
                    update(v, u, 0+1)
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    dfs(v)

            result = [0]*len(adj)
            sizes = [0]*len(adj)
            lookup = [False]*len(adj)
            prefix = [[] for _ in xrange(len(adj))]
            if k >= 0:
                dfs(0)
            return result

        def find_adj(edges):
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        adj2 = find_adj(edges2)
        mx = max(centroid_decomposition(adj2, k-1))
        adj1 = find_adj(edges1)
        return [mx+x for x in centroid_decomposition(adj1, k)]