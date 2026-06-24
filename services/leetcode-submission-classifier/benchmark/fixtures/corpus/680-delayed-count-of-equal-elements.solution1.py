# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delayed-count-of-equal-elements
# source_path: LeetCode-Solutions-master/Python/delayed-count-of-equal-elements.py
# solution_class: Solution
# submission_id: dcb0e79b5524512b2c168d3b71bf3f6e21e64e36
# seed: 2490843518

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def delayedCount(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0]*len(nums)
        cnt = collections.defaultdict(int)
        for i in reversed(xrange(len(nums)-k)):
            result[i] = cnt[nums[i]]
            cnt[nums[i+k]] += 1
        return result