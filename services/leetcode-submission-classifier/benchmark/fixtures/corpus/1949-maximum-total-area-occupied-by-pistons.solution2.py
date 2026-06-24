# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-area-occupied-by-pistons
# source_path: LeetCode-Solutions-master/Python/maximum-total-area-occupied-by-pistons.py
# solution_class: Solution2
# submission_id: 396f6f304c96e58e6ed8157b492ca978e5b5ff0a
# seed: 390841436

# Time:  O(h)
# Space: O(h)

import itertools


# line sweep, difference array

class Solution2(object):
    def maxArea(self, height, positions, directions):
        """
        :type height: int
        :type positions: List[int]
        :type directions: str
        :rtype: int
        """
        diff = collections.defaultdict(int)
        for d, i in itertools.izip(directions, positions):
            if d == 'U':
                diff[height-i] -= 1
                diff[(height-i)+height] += 1
            else:
                diff[i] += 1
                diff[i+height] -= 1
        result = total = sum(positions)
        cnt = directions.count('U')
        prev = 0
        for t, d in sorted(diff.iteritems()):
            total += (t-prev)*(-(len(directions)-cnt)+cnt)
            result = max(result, total)
            cnt += d
            prev = t
        return result