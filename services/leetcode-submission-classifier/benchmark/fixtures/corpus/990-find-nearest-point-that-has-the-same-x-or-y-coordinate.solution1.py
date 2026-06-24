# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-nearest-point-that-has-the-same-x-or-y-coordinate
# source_path: LeetCode-Solutions-master/Python/find-nearest-point-that-has-the-same-x-or-y-coordinate.py
# solution_class: Solution
# submission_id: 7f6cdfc4f1edfe1a78016e8a0127e9cf6ef2c9aa
# seed: 871654483

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        smallest, idx = float("inf"), -1
        for i, (r, c) in enumerate(points):
            dx, dy = x-r, y-c
            if dx*dy == 0 and abs(dx)+abs(dy) < smallest:
                smallest = abs(dx)+abs(dy)
                idx = i
        return idx