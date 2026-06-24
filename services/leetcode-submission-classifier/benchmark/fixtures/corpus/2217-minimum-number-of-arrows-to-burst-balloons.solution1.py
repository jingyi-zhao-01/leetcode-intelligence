# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-arrows-to-burst-balloons
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-arrows-to-burst-balloons.py
# solution_class: Solution
# submission_id: d81a547703751fe6a6affb755420ea7396f8eed5
# seed: 661057947

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()

        result = 0
        i = 0
        while i < len(points):
            j = i + 1
            right_bound = points[i][1]
            while j < len(points) and points[j][0] <= right_bound:
                right_bound = min(right_bound, points[j][1])
                j += 1
            result += 1
            i = j
        return result