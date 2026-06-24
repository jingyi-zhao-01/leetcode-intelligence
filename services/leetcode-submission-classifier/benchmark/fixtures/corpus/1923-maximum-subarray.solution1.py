# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-subarray.py
# solution_class: Solution
# submission_id: 89ce1ff165a6d9f2cc40cb507a7f9a5d2026950a
# seed: 3310754202

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, curr = float("-inf"), float("-inf")
        for x in nums:
            curr = max(curr+x, x)
            result = max(result, curr)
        return result