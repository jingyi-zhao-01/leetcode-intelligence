# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-visiting-all-points
# source_path: LeetCode-Solutions-master/Python/minimum-time-visiting-all-points.py
# solution_class: Solution
# submission_id: f1988eb062a6e2a2c266f543c2e589e165a32489
# seed: 1678786742

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return sum(max(abs(points[i+1][0] - points[i][0]),
                       abs(points[i+1][1] - points[i][1]))
                   for i in xrange(len(points)-1))