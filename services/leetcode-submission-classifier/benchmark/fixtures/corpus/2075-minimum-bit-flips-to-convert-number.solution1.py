# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-bit-flips-to-convert-number
# source_path: LeetCode-Solutions-master/Python/minimum-bit-flips-to-convert-number.py
# solution_class: Solution
# submission_id: 85421ebd1bec15983e4be0903eb58ed6d68f54b2
# seed: 3073659262

# Time:  O(logn)
# Space: O(1)

# bit manipulation

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return bin(start^goal).count('1')