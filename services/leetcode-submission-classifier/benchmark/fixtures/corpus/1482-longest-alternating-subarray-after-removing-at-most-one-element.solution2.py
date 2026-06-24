# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-alternating-subarray-after-removing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-alternating-subarray-after-removing-at-most-one-element.py
# solution_class: Solution2
# submission_id: 6a86a02bd717ee0fb87fc3a6745e41e272b583c3
# seed: 218910449

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = up0 = down0 = 1
        up1 = down1 = 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                up1, up0, down1, down0 = down1+1, down0+1, down0, 1
            elif nums[i] > nums[i+1]:
                up1, up0, down1, down0 = up0, 1, up1+1, up0+1
            else:
                up1, up0, down1, down0 = up0, 1, down0, 1
            result = max(result, up1, down1, up0, down0)
        return result