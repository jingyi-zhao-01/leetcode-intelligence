# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-threshold-path-with-limited-heavy-edges
# source_path: LeetCode-Solutions-master/Python/minimum-threshold-path-with-limited-heavy-edges.py
# solution_class: Solution
# submission_id: 30fd5b133f59240acfb3da2e9f06d4a1066dc330
# seed: 3571956648

# Time:  O((n + e) * loge)
# Space: O(n + e)

import collections


# binary search, 0-1 bfs, deque

class Solution(object):
    def minimumThreshold(self, n, edges, source, target, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type target: int
        :type k: int
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(i):
            t = weights[i]
            lookup = [False]*n
            dq = collections.deque([(source, 0)])
            while dq:
                u, d = dq.popleft()
                if lookup[u]:
                    continue
                lookup[u] = True
                if u == target:
                    return d <= k
                for v, w in adj[u]:
                    if w <= t:
                        dq.appendleft((v, d))
                    else:
                        dq.append((v, d+1))
            return False

        adj = [[] for _ in xrange(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        weights = sorted(set([0]+[w[2] for w in edges]))
        i = binary_search(0, len(weights)-1, check)
        return weights[i] if i < len(weights) else -1