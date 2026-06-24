# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-rectangles-to-cover-points
# source_path: LeetCode-Solutions-master/Python/minimum-rectangles-to-cover-points.py
# solution_class: Solution
# submission_id: 3fc92fad751cebd229467d14a29c620bdc22793b
# seed: 1608608137

# Time:  O(nlogn)
# Spade: O(n)

# sort, greedy

class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        result = 0
        left = -(w+1)
        for right, _ in points:
            if right-left <= w:
                continue
            left = right
            result += 1
        return result