# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fraction-addition-and-subtraction
# source_path: LeetCode-Solutions-master/Python/fraction-addition-and-subtraction.py
# solution_class: Solution
# submission_id: 42dc37aed3bdbe50e83e0fb4f54237423d665fd9
# seed: 227669353

# Time:  O(nlogx), x is the max denominator
# Space: O(n)

import re

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for i in xrange(0, len(ints), 2):
            a, b = ints[i], ints[i+1]
            A = A * b + a * B
            B *= b
            g = gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)