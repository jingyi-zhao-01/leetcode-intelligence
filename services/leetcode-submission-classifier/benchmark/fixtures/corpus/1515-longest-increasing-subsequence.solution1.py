# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-increasing-subsequence.py
# solution_class: Solution
# submission_id: 30940b3f156786332dcf13acb776caaa0dd5b8ba
# seed: 2392195366

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left = bisect.bisect_left(LIS, target)
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target
    
        for num in nums:
            insert(num)
        return len(LIS)