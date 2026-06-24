# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-semi-repeating-subarray
# source_path: LeetCode-Solutions-master/Python/longest-semi-repeating-subarray.py
# solution_class: Solution
# submission_id: a363bf6659c56253c22cf2f70b4cf8a249167bc8
# seed: 1115014846

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers

class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        result = left = repeat = 0
        for right in xrange(len(nums)):
            cnt[nums[right]] += 1
            if cnt[nums[right]] == 2:
                repeat += 1
            if repeat > k:
                if cnt[nums[left]] == 2:
                    repeat -= 1
                cnt[nums[left]] -= 1
                if not cnt[nums[left]]:
                    del cnt[nums[left]]
                left += 1
        return len(nums)-left