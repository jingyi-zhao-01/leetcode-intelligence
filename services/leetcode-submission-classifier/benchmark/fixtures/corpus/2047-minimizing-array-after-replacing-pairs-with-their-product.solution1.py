# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimizing-array-after-replacing-pairs-with-their-product
# source_path: LeetCode-Solutions-master/Python/minimizing-array-after-replacing-pairs-with-their-product.py
# solution_class: Solution
# submission_id: ea0afbbcf764f3ec5ec3bda08594839a50ae2f69
# seed: 1476454114

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minArrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if 0 in nums:
            return 1
        result = len(nums)
        curr = nums[0]
        for i in xrange(1, len(nums)):
            if curr*nums[i] > k:
                curr = nums[i]
            else:
                curr *= nums[i]
                result -= 1
        return result