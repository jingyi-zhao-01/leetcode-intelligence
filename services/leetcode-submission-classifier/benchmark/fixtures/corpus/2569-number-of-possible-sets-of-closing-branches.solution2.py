# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-possible-sets-of-closing-branches
# source_path: LeetCode-Solutions-master/Python/number-of-possible-sets-of-closing-branches.py
# solution_class: Solution2
# submission_id: 865611ed344bd0e2f0aaf78f2defdf73afb3006c
# seed: 4044867616

# Time:  O(r + 2^n * n^2)
# Space: O(n^3)

# graph, bitmasks, Floyd-Warshall algorithm, backtracking

class Solution2(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        def check(mask, dist):
            return all(dist[i][j] <= maxDistance for i in xrange(n) if mask&(1<<i) for j in xrange(i+1, n) if mask&(1<<j))

        def floydWarshall(mask, dist):
            for k in xrange(len(dist[0])):
                if mask&(1<<k) == 0:
                    continue
                for i in xrange(len(dist)):
                    if mask&(1<<i) == 0:  # optional, to speed up performance
                        continue
                    for j in xrange(i+1, len(dist[i])):
                        if mask&(1<<j) == 0:  # optional, to speed up performance
                             continue
                        dist[j][i] = dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
            return check(mask, dist)

        dist = [[0 if u == v else float("inf") for v in xrange(n)] for u in xrange(n)]
        for u, v, w in roads:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        return sum(floydWarshall(mask, [d[:] for d in dist]) for mask in xrange(1<<n))