# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-closest-number-to-zero
# source_path: LeetCode-Solutions-master/Python/find-closest-number-to-zero.py
# solution_class: Solution
# submission_id: 3e4ba3a0d035e66fd5bf317dc8ce2cefbc0dd343
# seed: 3558669231

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums, key=lambda x:(-abs(x), x))