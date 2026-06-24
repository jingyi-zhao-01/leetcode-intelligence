# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: solve-the-equation
# source_path: LeetCode-Solutions-master/Python/solve-the-equation.py
# solution_class: Solution
# submission_id: 3155f2040fbe0927e540aa0d447c62efb145f3b9
# seed: 1304744158

# Time:  O(n)
# Space: O(n)

import re

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        a, b, side = 0, 0, 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                a += side * int(sign + '1') * int(num or 1)
            elif num:
                b -= side * int(sign + num)
        return 'x=%d' % (b / a) if a else 'No solution' if b else 'Infinite solutions'