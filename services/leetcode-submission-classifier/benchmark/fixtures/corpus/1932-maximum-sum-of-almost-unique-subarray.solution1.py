# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-almost-unique-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-almost-unique-subarray.py
# solution_class: Solution
# submission_id: 3518ac007cf6c07abcb61cbc5517bb8d188f5b21
# seed: 1481264988

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers, sliding window

class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        lookup = collections.Counter()
        result = curr = left = 0
        for right in xrange(len(nums)):
            curr += nums[right]
            lookup[nums[right]] += 1
            if right-left+1 == k+1:
                lookup[nums[left]] -= 1
                if lookup[nums[left]] == 0:
                    del lookup[nums[left]]
                curr -= nums[left]
                left += 1
            if right-left+1 == k and len(lookup) >= m:
                result = max(result, curr)
        return result