# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-area-rectangle
# source_path: LeetCode-Solutions-master/Python/minimum-area-rectangle.py
# solution_class: Solution2
# submission_id: 1ee522a79124d7a0299885f95a08835df042bbd4
# seed: 2587780279

# Time:  O(n^1.5) on average
#        O(n^2) on worst
# Space: O(n)

import collections

class Solution2(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        lookup = set()
        result = float("inf")
        for x1, y1 in points:
            for x2, y2 in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    result = min(result, abs(x1-x2) * abs(y1-y2))
            lookup.add((x1, y1))
        return result if result != float("inf") else 0