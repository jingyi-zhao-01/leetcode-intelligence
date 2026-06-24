# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-semi-repeating-subarray
# source_path: LeetCode-Solutions-master/Python/longest-semi-repeating-subarray.py
# solution_class: Solution2
# submission_id: 849f8e6b5d731f5c4068e8c992b9c93a48a3162e
# seed: 3038296076

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers

class Solution2(object):
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
            while repeat > k:
                if cnt[nums[left]] == 2:
                    repeat -= 1
                cnt[nums[left]] -= 1
                if not cnt[nums[left]]:
                    del cnt[nums[left]]
                left += 1
            result = max(result, right-left+1)
        return result