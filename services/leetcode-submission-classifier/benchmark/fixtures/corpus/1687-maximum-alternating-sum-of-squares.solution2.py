# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-alternating-sum-of-squares
# source_path: LeetCode-Solutions-master/Python/maximum-alternating-sum-of-squares.py
# solution_class: Solution2
# submission_id: 220b13cffbf2dc8cbdac70d8290b2b78dcb630b6
# seed: 304047086

# Time:  O(n)
# Space: O(n)

import random


# greedy, quick select

class Solution2(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(x**2 for x in nums)
        return sum(arr)-2*sum(arr[i] for i in xrange(len(arr)//2))