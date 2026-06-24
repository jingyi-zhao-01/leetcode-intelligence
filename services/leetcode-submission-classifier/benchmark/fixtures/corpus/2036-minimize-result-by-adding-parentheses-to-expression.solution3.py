# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-result-by-adding-parentheses-to-expression
# source_path: LeetCode-Solutions-master/Python/minimize-result-by-adding-parentheses-to-expression.py
# solution_class: Solution3
# submission_id: ca11e63dfea7a452e597cd9cc2e01d3bbd0c4957
# seed: 3445997423

# Time:  O(n^2)
# Space: O(1)

import itertools


# brute force

class Solution3(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        best = None
        min_val = float("inf")
        pos = expression.index('+')
        for i in xrange(pos):
            for j in xrange(pos+1, len(expression)):
                val = (int(expression[:i] or "1")*
                       (int(expression[i:pos])+int(expression[pos+1:j+1]))*
                       int(expression[j+1:] or "1"))  # Space: O(n)
                if val < min_val:
                    min_val = val
                    best = (i, j)
        return "".join([expression[:best[0]], '(', expression[best[0]:best[1]+1], ')', expression[best[1]+1:]])  # Space: O(n)