# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: degree-of-an-array
# source_path: LeetCode-Solutions-master/Python/degree-of-an-array.py
# solution_class: Solution
# submission_id: e3434b722d9c36830a5b5b89582d9425aa7d3052
# seed: 1849817308

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        left, right = {}, {}
        for i, num in enumerate(nums):
            left.setdefault(num, i)
            right[num] = i
        degree = max(counts.values())
        return min(right[num]-left[num]+1 \
                   for num in counts.keys() \
                   if counts[num] == degree)