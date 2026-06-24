# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-longest-equal-subarray
# source_path: LeetCode-Solutions-master/Python/find-the-longest-equal-subarray.py
# solution_class: Solution
# submission_id: 839a218185c140314c994dca48262f15d925842d
# seed: 2597489811

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers, sliding window

class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter()
        result = left = 0
        for right in xrange(len(nums)):
            cnt[nums[right]] += 1
            result = max(result, cnt[nums[right]])
            if right-left+1 > result+k:
                cnt[nums[left]] -= 1
                left += 1
        return result