# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-element-in-an-array-after-merge-operations
# source_path: LeetCode-Solutions-master/Python/largest-element-in-an-array-after-merge-operations.py
# solution_class: Solution
# submission_id: 39ad339e663ad14797c5c2756a188b19878b3416
# seed: 2071445250

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for i in reversed(xrange(len(nums))):
            if nums[i] > curr:
                curr = 0
            curr += nums[i]
            result = max(result, curr)
        return result