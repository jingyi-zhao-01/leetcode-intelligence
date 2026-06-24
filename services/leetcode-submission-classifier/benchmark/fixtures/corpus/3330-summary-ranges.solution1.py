# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: summary-ranges
# source_path: LeetCode-Solutions-master/Python/summary-ranges.py
# solution_class: Solution
# submission_id: ab944c9156301e583d5c23410fef8c2531e0c439
# seed: 3562581152

# Time:  O(n)
# Space: O(1)

import itertools
import re

class Solution(object):
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]

        return ranges