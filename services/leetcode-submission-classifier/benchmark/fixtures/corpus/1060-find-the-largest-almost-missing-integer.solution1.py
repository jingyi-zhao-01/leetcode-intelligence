# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-largest-almost-missing-integer
# source_path: LeetCode-Solutions-master/Python/find-the-largest-almost-missing-integer.py
# solution_class: Solution
# submission_id: f4f9526459aa760096b98109c2196ce0ab6d0f83
# seed: 2001585679

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(nums):
            return max(nums)
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        if k == 1:
            return max(x for x, v in cnt.iteritems() if v == 1) if any(v == 1 for v in cnt.itervalues()) else -1
        result = -1
        if cnt[nums[0]] == 1:
            result = max(result, nums[0])
        if cnt[nums[-1]] == 1:
            result = max(result, nums[-1])
        return result