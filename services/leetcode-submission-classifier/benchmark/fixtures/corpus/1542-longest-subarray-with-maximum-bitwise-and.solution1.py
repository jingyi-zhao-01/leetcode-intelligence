# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subarray-with-maximum-bitwise-and
# source_path: LeetCode-Solutions-master/Python/longest-subarray-with-maximum-bitwise-and.py
# solution_class: Solution
# submission_id: 0ddeb525032eaa4aa8c415242a0732b45bef34e3
# seed: 1716535578

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        result, l = 1, 0
        for x in nums:
            if x == mx:
                l += 1
                result = max(result, l)
            else:
                l = 0
        return result