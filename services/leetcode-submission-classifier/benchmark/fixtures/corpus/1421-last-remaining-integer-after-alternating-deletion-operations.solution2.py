# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-remaining-integer-after-alternating-deletion-operations
# source_path: LeetCode-Solutions-master/Python/last-remaining-integer-after-alternating-deletion-operations.py
# solution_class: Solution
# submission_id: 12c2d119c886528f50d5a46900a90e5b6674e14a
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
        result = l = 1
        p = 0
        while n != 1:
            if p and not n%2:
                result += l
            n = (n+1)//2
            l <<= 1
            p ^= 1
        return result