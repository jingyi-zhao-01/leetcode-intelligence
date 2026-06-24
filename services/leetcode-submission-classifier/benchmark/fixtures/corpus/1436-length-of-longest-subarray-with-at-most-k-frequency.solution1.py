# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-longest-subarray-with-at-most-k-frequency
# source_path: LeetCode-Solutions-master/Python/length-of-longest-subarray-with-at-most-k-frequency.py
# solution_class: Solution
# submission_id: 7169c1a99ed1137d61f8f1ce18f877301b0ff069
# seed: 3958592745

# Time:  O(n)
# Space: o(n)

import collections


# freq table, two pointers, sliding window

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter()
        result = left = 0
        for right in xrange(len(nums)):
            cnt[nums[right]] += 1
            while not (cnt[nums[right]] <= k):
                cnt[nums[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result