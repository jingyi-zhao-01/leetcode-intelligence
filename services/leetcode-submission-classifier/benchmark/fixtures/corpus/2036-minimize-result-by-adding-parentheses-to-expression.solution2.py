# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-result-by-adding-parentheses-to-expression
# source_path: LeetCode-Solutions-master/Python/minimize-result-by-adding-parentheses-to-expression.py
# solution_class: Solution2
# submission_id: 8f22bf0ad8f25c9ed8970f986825c78ffd5ffd0c
# seed: 4110485199

# Time:  O(n^2)
# Space: O(1)

import itertools


# brute force

class Solution2(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        best = None
        min_val = float("inf")
        pos = expression.index('+')
        left, right = int(expression[0:pos]), int(expression[pos+1:])  # Space: O(n)
        base1, base2_init = 10**pos, 10**(len(expression)-(pos+1)-1)
        for i in xrange(pos):
            base2 = base2_init
            for j in xrange(pos+1, len(expression)):
                a, b = divmod(left, base1)
                c, d = divmod(right, base2)
                val = max(a, 1)*(b+c)*max(d, 1)
                if val < min_val:
                    min_val = val
                    best = (i, j)
                base2 //= 10
            base1 //= 10
        return "".join([expression[:best[0]], '(', expression[best[0]:best[1]+1], ')', expression[best[1]+1:]])  # Space: O(n)