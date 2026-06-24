# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# source_path: LeetCode-Solutions-master/Python/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py
# solution_class: Solution2
# submission_id: 65817ff515450c3ae07bdf38080fa773bd8d7301
# seed: 582931532

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_dq, min_dq = collections.deque(), collections.deque()
        result, left = 0, 0
        for right, num in enumerate(nums):
            while max_dq and nums[max_dq[-1]] <= num:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= num:
                min_dq.pop()
            min_dq.append(right)
            while nums[max_dq[0]]-nums[min_dq[0]] > limit:  # both always exist "right" element
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            result = max(result, right-left+1)
        return result