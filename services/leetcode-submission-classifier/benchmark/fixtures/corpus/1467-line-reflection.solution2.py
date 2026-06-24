# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: line-reflection
# source_path: LeetCode-Solutions-master/Python/line-reflection.py
# solution_class: Solution2
# submission_id: a9d9002a4c7c263a2fe2b3e689c6bb9c336fbd0e
# seed: 3579665370

# Time:  O(n)
# Space: O(n)

import collections


# Hash solution.

class Solution2(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        points.sort()
        # Space: O(n)
        points[len(points)/2:] = sorted(points[len(points)/2:], \
                                        lambda x, y: y[1] - x[1] if x[0] == y[0] else \
                                                     x[0] - y[0])
        mid = points[0][0] + points[-1][0]
        left, right = 0, len(points) - 1
        while left <= right:
            if (mid != points[left][0] + points[right][0]) or \
               (points[left][0] != points[right][0] and \
                points[left][1] != points[right][1]):
                return False
            left += 1
            right -= 1
        return True