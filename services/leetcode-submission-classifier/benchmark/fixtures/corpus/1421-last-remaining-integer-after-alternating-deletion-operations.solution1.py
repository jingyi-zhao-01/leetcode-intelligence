# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-remaining-integer-after-alternating-deletion-operations
# source_path: LeetCode-Solutions-master/Python/last-remaining-integer-after-alternating-deletion-operations.py
# solution_class: Solution
# submission_id: 8b2e5c7b1b958c40a2143b0c6f717a62a305f9ff
# seed: 3681801426

# Time:  O(1)
# Space: O(1)

# bitmasks

class Solution(object):
    def lastInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        MASK = 0xAAAAAAAAAAAAA
        return ((n-1)&MASK)+1