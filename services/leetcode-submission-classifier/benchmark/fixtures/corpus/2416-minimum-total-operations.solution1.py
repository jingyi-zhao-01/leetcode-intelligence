# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-total-operations
# source_path: LeetCode-Solutions-master/Python/minimum-total-operations.py
# solution_class: Solution
# submission_id: 4a0d72ce0eeb369dbb0ce9ce01dc5697b83fa332
# seed: 2362152359

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums[i] != nums[i+1] for i in xrange(len(nums)-1))