# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-number-with-alternating-bits
# source_path: LeetCode-Solutions-master/Python/binary-number-with-alternating-bits.py
# solution_class: Solution
# submission_id: a4262bc18d436a2ecd80904b5e64564b2a72b844
# seed: 4293589177

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n, curr = divmod(n, 2)
        while n > 0:
            if curr == n % 2:
                return False
            n, curr = divmod(n, 2)
        return True