# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-array-concatenation-value
# source_path: LeetCode-Solutions-master/Python/find-the-array-concatenation-value.py
# solution_class: Solution
# submission_id: dee64962347adb47650310ed463051d208f46db9
# seed: 1234118931

# Time:  O(nlogr)
# Space: O(1)

import math


# math

class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((nums[i]*10**(int(math.log10(nums[~i]))+1) for i in xrange(len(nums)//2)))+sum(nums[i] for i in xrange(len(nums)//2, len(nums)))