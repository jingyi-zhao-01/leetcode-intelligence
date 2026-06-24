# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-median-of-array-equal-to-k
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-median-of-array-equal-to-k.py
# solution_class: Solution2
# submission_id: dc58c98ce948300cc9b308c595c3a97a48f85cb1
# seed: 3254110863

# Time:  O(n)
# Space: O(1)

import random


# quick select, greedy

class Solution2(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return (sum(max(nums[i]-k, 0) for i in xrange(len(nums)//2+1))+
                sum(max(k-nums[i], 0) for i in xrange(len(nums)//2, len(nums))))