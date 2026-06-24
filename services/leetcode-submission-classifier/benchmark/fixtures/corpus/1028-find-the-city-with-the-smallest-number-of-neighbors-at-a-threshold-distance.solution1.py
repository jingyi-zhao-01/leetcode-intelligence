# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
# source_path: LeetCode-Solutions-master/Python/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance.py
# solution_class: Solution
# submission_id: 1f10b2f14701a2f907b16d8be2e262f0cec2fef8
# seed: 1575924863

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = [[float("inf")]*n for _ in xrange(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w
        for i in xrange(n):
            dist[i][i] = 0
        for k in xrange(n): 
            for i in xrange(n): 
                for j in xrange(n): 
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]) 
        result = {sum(d <= distanceThreshold for d in dist[i]): i for i in xrange(n)}
        return result[min(result.iterkeys())]