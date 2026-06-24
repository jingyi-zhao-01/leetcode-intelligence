# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-convert-string-i
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-convert-string-i.py
# solution_class: Solution2
# submission_id: 01dc17b59ec43382aa6c003de0ae7ac09e8c4b19
# seed: 3675647373

# Time:  O(o + k * eloge + n), k = len(set(original)), e is the number of edges reachable from a given node u
# Space: O(o + k * v), v is the number of nodes reachable from a given node u

import heapq


# dijkstra's algorithm, memoization

class Solution2(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = float("inf")
        def floydWarshall(dist):
            for k in xrange(len(dist)):
                for i in xrange(len(dist)):
                    if dist[i][k] == INF:
                        continue
                    for j in xrange(len(dist[i])):
                        if dist[k][j] == INF:
                            continue
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        dist = [[0 if u == v else INF for v in xrange(26)] for u in xrange(26)]
        for i in xrange(len(original)):
            u, v = ord(original[i])-ord('a'), ord(changed[i])-ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        floydWarshall(dist)
        result = sum(dist[ord(source[i])-ord('a')][ord(target[i])-ord('a')] for i in xrange(len(source)))
        return result if result != INF else -1