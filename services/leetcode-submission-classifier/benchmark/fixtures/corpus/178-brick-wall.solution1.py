# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: brick-wall
# source_path: LeetCode-Solutions-master/Python/brick-wall.py
# solution_class: Solution
# submission_id: 2780197bc13924b4416ab8cb5e7b673ef918a006
# seed: 3172576488

# Time:  O(n), n is the total number of the bricks
# Space: O(m), m is the total number different widths

import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        widths = collections.defaultdict(int)
        result = len(wall)
        for row in wall:
            width = 0
            for i in xrange(len(row)-1):
                width += row[i]
                widths[width] += 1
                result = min(result, len(wall) - widths[width])
        return result