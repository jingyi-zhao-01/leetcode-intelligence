# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shuffle-an-array
# source_path: LeetCode-Solutions-master/Python/shuffle-an-array.py
# solution_class: Solution
# submission_id: c3413dbf993f9de824116ef0b3fe41939bd0d017
# seed: 3290297760

# Time:  O(n)
# Space: O(n)

import random

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.__nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = list(self.__nums)
        for i in xrange(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums