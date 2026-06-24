# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: integer-replacement
# source_path: LeetCode-Solutions-master/Python/integer-replacement.py
# solution_class: Solution
# submission_id: 7f72c743bb2db35dfe0b00f393ec9bf39fd56a6f
# seed: 735575168

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 1:
            b = n & 3
            if n == 3:
                n -= 1
            elif b == 3:
                n += 1
            elif b == 1:
                n -= 1
            else:
                n /= 2
            result += 1

        return result