# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subsequence-with-non-zero-bitwise-xor
# source_path: LeetCode-Solutions-master/Python/longest-subsequence-with-non-zero-bitwise-xor.py
# solution_class: Solution
# submission_id: f6fd4f0815f1dd166385994d60916e92b2777de1
# seed: 3537573178

# Time:  O(n)
# Space: O(1)

# bitmasks

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)-int(reduce(lambda accu, x: accu^x, nums, 0) == 0) if any(x for x in nums) else 0