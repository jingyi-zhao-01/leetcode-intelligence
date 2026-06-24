# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-change-the-final-value-of-expression
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-change-the-final-value-of-expression.py
# solution_class: Solution
# submission_id: f8f4bce7b0f4fc13d948dbce67e8be720215f800
# seed: 2572435716

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def compute(operands, operators):
            right, left = operands.pop(), operands.pop()
            operands.append(ops[operators.pop()](left, right))

        ops = {'&':lambda x, y: [min(x[0], y[0]), min(x[1]+y[1], min(x[1], y[1])+1)],
               '|':lambda x, y: [min(x[0]+y[0], min(x[0], y[0])+1), min(x[1], y[1])]}
        precedence = {'&':0, '|':0}
        operands, operators = [], []
        for c in expression:
            if c.isdigit():
                operands.append([int(c != '0'), int(c != '1')])
            elif c == '(':
                operators.append(c)
            elif c == ')':
                while operators[-1] != '(':
                    compute(operands, operators)
                operators.pop()
            elif c in precedence:
                while operators and operators[-1] in precedence and \
                      precedence[operators[-1]] >= precedence[c]:
                    compute(operands, operators)
                operators.append(c)
        while operators:
            compute(operands, operators)
        return max(operands[-1])