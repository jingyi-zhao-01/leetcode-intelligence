# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cinema-seat-allocation
# source_path: LeetCode-Solutions-master/Python/cinema-seat-allocation.py
# solution_class: Solution
# submission_id: 66fd25942c93c652472dd407c56125ad1162d60a
# seed: 3559342820

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        lookup = collections.defaultdict(lambda: [False]*3)
        for r, c in reservedSeats:
            if 2 <= c <= 5:
                lookup[r][0] = True
            if 4 <= c <= 7:
                lookup[r][1] = True
            if 6 <= c <= 9:
                lookup[r][2] = True
        result = 2*n
        for a, b, c in lookup.itervalues():
            if not a and not c:
                continue
            if not a or not b or not c:
                result -= 1
                continue
            result -= 2
        return result