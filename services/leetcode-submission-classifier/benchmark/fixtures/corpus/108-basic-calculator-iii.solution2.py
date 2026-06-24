# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: basic-calculator-iii
# source_path: LeetCode-Solutions-master/Python/basic-calculator-iii.py
# solution_class: Solution2
# submission_id: 1b70d77341610c4d3c2ca289fa28b8c9ccf91edf
# seed: 901170209

# Time:  O(n)
# Space: O(n)

import operator

class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)