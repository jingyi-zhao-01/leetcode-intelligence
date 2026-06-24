# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-ways-to-partition-an-array
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-ways-to-partition-an-array.py
# solution_class: Solution
# submission_id: 21a2d02c030bad730d281e75070d1923df5bf6cc
# seed: 1955370109

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(nums)
        right = collections.Counter()
        prefix = 0
        for i in xrange(len(nums)-1):
            prefix += nums[i]
            right[prefix-(total-prefix)] += 1
        result = right[0]
        left = collections.Counter()
        prefix = 0
        for x in nums:
            result = max(result, left[k-x]+right[-(k-x)])
            prefix += x
            left[prefix-(total-prefix)] += 1
            right[prefix-(total-prefix)] -= 1
        return result