# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ways-to-split-array-into-good-subarrays
# source_path: LeetCode-Solutions-master/Python/ways-to-split-array-into-good-subarrays.py
# solution_class: Solution
# submission_id: 76a694621d752015c057d497cbb86c1ea4b5e116
# seed: 248637523

# Time:  O(n)
# Space: O(1)

# combinatorics

class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        result, prev = 1, -1
        for i in xrange(len(nums)):
            if nums[i] != 1:
                continue
            if prev != -1:
                result = (result*(i-prev))%MOD
            prev = i
        return result if prev != -1 else 0