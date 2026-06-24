# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-partition-factor
# source_path: LeetCode-Solutions-master/Python/maximum-partition-factor.py
# solution_class: Solution3
# submission_id: 764547aac10af5e176739dc52b3af2b993b65079
# seed: 3021445921

# Time:  O(n^2 * logn)
# Space: O(n^2)

# greedy, sort, union find with parity

class Solution3(object):
    def maxPartitionFactor(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        INF = float("inf")
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def dist(u, v):
            return abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])

        def is_bipartite(d):
            def bfs(u):
                if lookup[u] != -1:
                    return True
                lookup[u] = 0
                q = [u]
                while q:
                    new_q = []
                    for u in q:
                        for v in xrange(len(points)):
                            if not (v != u and dist(v, u) < d):
                                continue
                            if lookup[v] != -1:
                                if lookup[v] != lookup[u]^1:
                                    return False
                                continue
                            lookup[v] = lookup[u]^1
                            new_q.append(v)
                    q = new_q
                return True 

            lookup = [-1]*len(points)
            return all(bfs(u) for u in xrange(len(points)))

        sorted_dists = sorted({dist(u, v) for u in xrange(len(points)) for v in xrange(u+1, len(points))}|{INF})
        left, right = 0, len(sorted_dists)-1
        result = binary_search_right(left, right, lambda i: is_bipartite(sorted_dists[i]))
        return sorted_dists[result] if sorted_dists[result] != INF else 0