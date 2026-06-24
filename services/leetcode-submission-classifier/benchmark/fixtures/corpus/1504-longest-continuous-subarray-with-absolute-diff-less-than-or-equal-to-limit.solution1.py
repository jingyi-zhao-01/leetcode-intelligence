# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# source_path: LeetCode-Solutions-master/Python/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py
# solution_class: Solution
# submission_id: c038b77ae144be30ba92ce8d47d9efc4ca4fcf74
# seed: 3803000826

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_dq, min_dq = collections.deque(), collections.deque()
        left = 0
        for right, num in enumerate(nums):
            while max_dq and nums[max_dq[-1]] <= num:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= num:
                min_dq.pop()
            min_dq.append(right)
            if nums[max_dq[0]]-nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1  # advance left by one to not count in result
        return len(nums)-left