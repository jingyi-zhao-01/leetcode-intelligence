# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-four
# source_path: LeetCode-Solutions-master/Python/power-of-four.py
# solution_class: Solution
# submission_id: 343d9294b20162383b07cbf18263b10c0b4eb6bc
# seed: 1609577757

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)