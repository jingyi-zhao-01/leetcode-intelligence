# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-xor-sum-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/minimum-xor-sum-of-two-arrays.py
# solution_class: Solution
# submission_id: d4b849c6f8791a179aa71b53055b4c56cdb27ada
# seed: 3399186271

# Time:  O(n^3)
# Space: O(n^2)

# weighted bipartite matching solution

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        # Template translated from:
        # https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/WeightedMatching.h
        def hungarian(a):  # Time: O(n^2 * m), Space: O(n + m)
            if not a:
                return 0, []
            n, m = len(a)+1, len(a[0])+1
            u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
            for i in xrange(1, n):
                p[0] = i
                j0 = 0  # add "dummy" worker 0
                dist, pre = [float("inf")]*m, [-1]*m
                done = [False]*(m+1)
                while True:  # dijkstra
                    done[j0] = True
                    i0, j1, delta = p[j0], None, float("inf")
                    for j in xrange(1, m):
                        if done[j]:
                            continue
                        cur = a[i0-1][j-1]-u[i0]-v[j]
                        if cur < dist[j]:
                            dist[j], pre[j] = cur, j0
                        if dist[j] < delta:
                            delta, j1 = dist[j], j
                    for j in xrange(m):
                        if done[j]:
                            u[p[j]] += delta
                            v[j] -= delta
                        else:
                            dist[j] -= delta
                    j0 = j1
                    if not p[j0]:
                        break
                while j0:  # update alternating path
                    j1 = pre[j0]
                    p[j0], j0 = p[j1], j1
            for j in xrange(1, m):
                if p[j]:
                    ans[p[j]-1] = j-1
            return -v[0], ans  # min cost
        
        adj = [[0]*len(nums2) for _ in xrange(len(nums1))]
        for i in xrange(len(nums1)):
            for j in xrange(len(nums2)):
                adj[i][j] = nums1[i]^nums2[j]
        return hungarian(adj)[0]