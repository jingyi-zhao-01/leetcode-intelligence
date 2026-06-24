# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-triangle-area
# source_path: LeetCode-Solutions-master/Python/largest-triangle-area.py
# solution_class: Solution
# submission_id: 39d6218fbcd3f677f8911cdd4ab022ccabebdff9
# seed: 1319113848

# Time:  O(n^3)
# Space: O(1)

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        result = 0
        for i in xrange(len(points)-2):
            for j in xrange(i+1, len(points)-1):
                for k in xrange(j+1, len(points)):
                    result = max(result,
                                 0.5 * abs(points[i][0] * points[j][1] +
                                           points[j][0] * points[k][1] +
                                           points[k][0] * points[i][1] -
                                           points[j][0] * points[i][1] -
                                           points[k][0] * points[j][1] -
                                           points[i][0] * points[k][1]))
        return result