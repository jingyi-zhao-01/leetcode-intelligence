# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wiggle-subsequence
# source_path: LeetCode-Solutions-master/Python/wiggle-subsequence.py
# solution_class: Solution
# submission_id: 9a089902a48f8bf47e9ee29cdc022dd77c35567b
# seed: 1684492303

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        length, up = 1, None

        for i in xrange(1, len(nums)):
            if nums[i - 1] < nums[i] and (up is None or up is False):
                length += 1
                up = True
            elif nums[i - 1] > nums[i] and (up is None or up is True):
                length += 1
                up = False

        return length