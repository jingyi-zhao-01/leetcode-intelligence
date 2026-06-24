# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-where-max-element-appears-at-least-k-times
# source_path: LeetCode-Solutions-master/Python/count-subarrays-where-max-element-appears-at-least-k-times.py
# solution_class: Solution
# submission_id: 549ffcb30031f04a3707fe31db2c39e0c87813a6
# seed: 3374721750

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        result = left = cnt = 0
        for right in xrange(len(nums)):
            cnt += int(nums[right] == mx)
            while cnt == k:
                cnt -= int(nums[left] == mx)
                left += 1
            result += left
        return result