# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-reverse-polish-notation
# source_path: LeetCode-Solutions-master/Python/evaluate-reverse-polish-notation.py
# solution_class: Solution
# submission_id: 87596eba8acdc181fbe5fded97a43aeefdc607cc
# seed: 2918661548

# Time:  O(n)
# Space: O(n)

import operator

class Solution(object):
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token not in operators:
                numerals.append(int(token))
            else:
                y, x = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](x * 1.0, y)))
        return numerals.pop()