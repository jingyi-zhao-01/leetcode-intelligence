# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-the-rectangle
# source_path: LeetCode-Solutions-master/Python/construct-the-rectangle.py
# solution_class: Solution
# submission_id: 713be19ed70cb47003b0c8ed02a2696234da091b
# seed: 819821922

# Time:  O(1)
# Space: O(1)

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]