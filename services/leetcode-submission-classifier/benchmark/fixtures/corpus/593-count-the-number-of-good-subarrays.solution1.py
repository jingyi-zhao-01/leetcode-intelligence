# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-good-subarrays
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-good-subarrays.py
# solution_class: Solution
# submission_id: f7999c6fc87bc45efaa612a9e7c1cd60c9e77b0c
# seed: 2807728895

# Time:  O(n)
# Space: O(n)

import collections


# two pointers, sliding window

class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = curr = left = 0
        cnt = collections.Counter()
        for right in xrange(len(nums)):
            curr += cnt[nums[right]]
            cnt[nums[right]] += 1
            while curr >= k:
                cnt[nums[left]] -= 1
                curr -= cnt[nums[left]]
                left += 1
            result += left
        return result