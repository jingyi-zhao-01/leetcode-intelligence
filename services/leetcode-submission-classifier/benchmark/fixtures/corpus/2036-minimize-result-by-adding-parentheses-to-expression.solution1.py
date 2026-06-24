# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-result-by-adding-parentheses-to-expression
# source_path: LeetCode-Solutions-master/Python/minimize-result-by-adding-parentheses-to-expression.py
# solution_class: Solution
# submission_id: a620280062396f4a7f5fe81146969deced104ec7
# seed: 3918613926

# Time:  O(n^2)
# Space: O(1)

import itertools


# brute force

class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def stoi(s, i, j):
            result = 0
            for k in xrange(i, j):
                result = result*10+(ord(s[k])-ord('0'))
            return result

        best = None
        min_val = float("inf")
        pos = expression.index('+')
        left, right = stoi(expression, 0, pos), stoi(expression, pos+1, len(expression))
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
        return "".join(itertools.chain((expression[i] for i in xrange(best[0])),
                                       '(', (expression[i] for i in xrange(best[0], best[1]+1)), ')',
                                       (expression[i] for i in xrange(best[1]+1, len(expression)))))