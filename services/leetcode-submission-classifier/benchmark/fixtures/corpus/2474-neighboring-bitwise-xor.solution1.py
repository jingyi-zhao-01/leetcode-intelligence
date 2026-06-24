# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: neighboring-bitwise-xor
# source_path: LeetCode-Solutions-master/Python/neighboring-bitwise-xor.py
# solution_class: Solution
# submission_id: b00ac56b2592548c2b51caa3297012030ec6719a
# seed: 3985222612

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        return reduce(lambda total, x: total^x, derived, 0) == 0