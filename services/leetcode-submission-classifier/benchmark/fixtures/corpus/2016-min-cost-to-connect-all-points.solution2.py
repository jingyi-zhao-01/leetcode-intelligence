# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: min-cost-to-connect-all-points
# source_path: LeetCode-Solutions-master/Python/min-cost-to-connect-all-points.py
# solution_class: Solution2
# submission_id: 6dccd4c8c7acfb92f535cd1df38e6b81f9e35af0
# seed: 2774141765

# Time:  O(n^2)
# Space: O(n)

class Solution2(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edges = []
        for u in xrange(len(points)):
            for v in xrange(u+1, len(points)):
                edges.append((u, v, abs(points[v][0]-points[u][0]) + abs(points[v][1]-points[u][1])))
        edges.sort(key=lambda x: x[2])
        result = 0
        union_find = UnionFind(len(points))
        for u, v, val in edges:
            if union_find.union_set(u, v):
                result += val
        return result