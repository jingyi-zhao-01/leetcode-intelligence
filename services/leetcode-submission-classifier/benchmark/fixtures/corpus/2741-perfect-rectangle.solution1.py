# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: perfect-rectangle
# source_path: LeetCode-Solutions-master/Python/perfect-rectangle.py
# solution_class: Solution
# submission_id: b4d0215fabb2996f78b4072463320239071a5413
# seed: 1798768719

# Time:  O(n)
# Space: O(n)

from collections import defaultdict

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(rec[0] for rec in rectangles)
        bottom = min(rec[1] for rec in rectangles)
        right = max(rec[2] for rec in rectangles)
        top = max(rec[3] for rec in rectangles)

        points = defaultdict(int)
        for l, b, r, t in rectangles:
            for p, q in zip(((l, b), (r, b), (l, t), (r, t)), (1, 2, 4, 8)):
                if points[p] & q:
                    return False
                points[p] |= q

        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 5, 10, 12, 15):
                    return False

        return True