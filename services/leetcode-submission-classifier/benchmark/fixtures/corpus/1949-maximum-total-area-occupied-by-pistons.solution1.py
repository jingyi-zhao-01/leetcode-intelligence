# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-area-occupied-by-pistons
# source_path: LeetCode-Solutions-master/Python/maximum-total-area-occupied-by-pistons.py
# solution_class: Solution
# submission_id: 318e0e113ad2e90ef7d3f52ce11af20aee743555
# seed: 2315203795

# Time:  O(h)
# Space: O(h)

import itertools


# line sweep, difference array

class Solution(object):
    def maxArea(self, height, positions, directions):
        """
        :type height: int
        :type positions: List[int]
        :type directions: str
        :rtype: int
        """
        diff = [0]*(2*height+1)
        for d, i in itertools.izip(directions, positions):
            if d == 'U':
                diff[height-i] -= 1
                diff[(height-i)+height] += 1
            else:
                diff[i] += 1
                diff[i+height] -= 1
        result = total = sum(positions)
        cnt = directions.count('U')
        for t in xrange(1, len(diff)):
            total += -(len(directions)-cnt)+cnt
            result = max(result, total)
            cnt += diff[t]
        return result