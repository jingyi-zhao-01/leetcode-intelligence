# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-alternating-subarray-after-removing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-alternating-subarray-after-removing-at-most-one-element.py
# solution_class: Solution
# submission_id: 3f95bf81e4ad12bd54b709b6de3c5a02c7a7b547
# seed: 1887766413

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = up1 = up0 = down1 = down0 = 1
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                up1, up0, down1, down0 = down1+1, down0+1, down0, 1
            elif nums[i] > nums[i+1]:
                up1, up0, down1, down0 = up0, 1, up1+1, up0+1
            else:
                up1, up0, down1, down0 = up0, 1, down0, 1
            result = max(result, up1, down1)
        return result