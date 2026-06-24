# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-triangle-number
# source_path: LeetCode-Solutions-master/Python/valid-triangle-number.py
# solution_class: Solution
# submission_id: 7ccc226df81d41853ce1098e07ca53e97f43d6a1
# seed: 789914046

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in reversed(xrange(2, len(nums))):
            left, right = 0, i-1
            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    result += right-left
                    right -= 1
                else:
                    left += 1
        return result