# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: basic-calculator-iii
# source_path: LeetCode-Solutions-master/Python/basic-calculator-iii.py
# solution_class: Solution
# submission_id: 953ccf0e7bdabd29e1834655bdfd7df3b654d1e2
# seed: 2522429796

# Time:  O(n)
# Space: O(n)

import operator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def compute(operands, operators):
            right, left = operands.pop(), operands.pop()
            operands.append(ops[operators.pop()](left, right))

        ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
        precedence = {'+':0, '-':0, '*':1, '/':1}
        operands, operators, operand = [], [], 0
        for i in xrange(len(s)):
            if s[i].isdigit():
                operand = operand*10 + int(s[i])
                if i == len(s)-1 or not s[i+1].isdigit():
                    operands.append(operand)
                    operand = 0
            elif s[i] == '(':
                operators.append(s[i])
            elif s[i] == ')':
                while operators[-1] != '(':
                    compute(operands, operators)
                operators.pop()
            elif s[i] in precedence:
                while operators and operators[-1] in precedence and \
                      precedence[operators[-1]] >= precedence[s[i]]:
                    compute(operands, operators)
                operators.append(s[i])
        while operators:
            compute(operands, operators)
        return operands[-1]