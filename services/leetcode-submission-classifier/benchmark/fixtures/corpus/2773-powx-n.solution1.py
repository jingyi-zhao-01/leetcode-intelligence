# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: powx-n
# source_path: LeetCode-Solutions-master/Python/powx-n.py
# solution_class: Solution
# submission_id: 4a1b560365af491b8d7cececcf14e65f41ec6066
# seed: 1825700817

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n >>= 1
            x *= x

        return 1 / result if n < 0 else result