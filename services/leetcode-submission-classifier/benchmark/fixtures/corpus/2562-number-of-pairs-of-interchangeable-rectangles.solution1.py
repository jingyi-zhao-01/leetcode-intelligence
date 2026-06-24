# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-pairs-of-interchangeable-rectangles
# source_path: LeetCode-Solutions-master/Python/number-of-pairs-of-interchangeable-rectangles.py
# solution_class: Solution
# submission_id: f54009ec0ee1f24ae308bc554ed5cac04749299a
# seed: 1113694149

# Time:  O(n)
# Space: O(n)

import collections
import fractions

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for w, h in rectangles:
            g = fractions.gcd(w, h)  # Time: O(logx) ~= O(1)
            count[(w//g, h//g)] += 1
        return sum(c*(c-1)//2 for c in count.itervalues())