# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trionic-array-ii
# source_path: LeetCode-Solutions-master/Python/trionic-array-ii.py
# solution_class: Solution
# submission_id: f70492cf38db02e93798bdf519cd5caa0c70ffc2
# seed: 447943960

# Time:  O(n)
# Space: O(1)

# two pointers, greedy

class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float("-inf")
        left = p = q = 0
        prefix = nums[0]
        for right in xrange(1, len(nums)):
            prefix += nums[right]
            if nums[right-1] > nums[right]:
                if right-2 >= 0 and nums[right-2] < nums[right-1]:
                    p = right-1
                    while left < q or (nums[left] < 0 and left+1 < p):
                        prefix -= nums[left]
                        left += 1
            elif nums[right-1] < nums[right]:
                if right-2 >= 0 and nums[right-2] > nums[right-1]:
                    q = right-1
                if left != p:
                    result = max(result, prefix)
            else:
                left = p = q = right
                prefix = nums[right]
        return result