# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: min-cost-to-connect-all-points
# source_path: LeetCode-Solutions-master/Python/min-cost-to-connect-all-points.py
# solution_class: Solution
# submission_id: bed5adcf2f7b4e889eae55cd1c56e5456c93223b
# seed: 2424803636

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result, u = 0, 0  # we can start from any node as u
        dist = [float("inf")]*len(points)
        lookup = set()
        for _ in xrange(len(points)-1):
            x0, y0 = points[u]
            lookup.add(u)
            for v, (x, y) in enumerate(points):
                if v in lookup:
                    continue
                dist[v] = min(dist[v], abs(x-x0) + abs(y-y0))
            val, u = min((val, v) for v, val in enumerate(dist)) 
            dist[u] = float("inf")  # used
            result += val
        return result