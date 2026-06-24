# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equal-row-and-column-pairs
# source_path: LeetCode-Solutions-master/Python/equal-row-and-column-pairs.py
# solution_class: Solution
# submission_id: 5c039234c2238bb2ac61c9434b03b1d3979233c8
# seed: 716665562

# Time:  O(n^2)
# Space: O(n^2)

import collections
import itertools


# hash table

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt1 = collections.Counter(tuple(row) for row in grid)
        cnt2 = collections.Counter(tuple(col) for col in itertools.izip(*grid))
        return sum(cnt1[k]*cnt2[k] for k in cnt1.iterkeys() if k in cnt2)