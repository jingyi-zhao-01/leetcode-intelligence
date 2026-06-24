# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: how-many-numbers-are-smaller-than-the-current-number
# source_path: LeetCode-Solutions-master/Python/how-many-numbers-are-smaller-than-the-current-number.py
# solution_class: Solution
# submission_id: d4f46d5637fa5a4a1ba6c5c5b5ab8652ea2fbad3
# seed: 2354679110

# Time:  O(n + m), m is the max number of nums
# Space: O(m)

import collections

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        for i in xrange(max(nums)+1):
            count[i] += count[i-1]
        return [count[i-1] for i in nums]