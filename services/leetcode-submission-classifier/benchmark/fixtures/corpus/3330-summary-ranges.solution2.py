# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: summary-ranges
# source_path: LeetCode-Solutions-master/Python/summary-ranges.py
# solution_class: Solution2
# submission_id: f181ef525d317546b2d0098205e6fe189a2e361c
# seed: 1962961631

# Time:  O(n)
# Space: O(1)

import itertools
import re

class Solution2(object):
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        return [re.sub('->.*>', '->', '->'.join(repr(n) for _, n in g))
            for _, g in itertools.groupby(enumerate(nums), lambda i_n: i_n[1]-i_n[0])]