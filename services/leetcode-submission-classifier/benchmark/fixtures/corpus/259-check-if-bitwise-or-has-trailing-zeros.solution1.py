# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-bitwise-or-has-trailing-zeros
# source_path: LeetCode-Solutions-master/Python/check-if-bitwise-or-has-trailing-zeros.py
# solution_class: Solution
# submission_id: a38cf0b03de23cbdd6a2cd7cca082c98b58c010e
# seed: 3286565487

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(x%2 == 0 for x in nums) >= 2