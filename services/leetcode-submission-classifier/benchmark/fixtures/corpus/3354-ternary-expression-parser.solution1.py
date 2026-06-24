# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ternary-expression-parser
# source_path: LeetCode-Solutions-master/Python/ternary-expression-parser.py
# solution_class: Solution
# submission_id: 117f5ee48629305c4793766a1afc15208ccf34b7
# seed: 2749580234

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""

        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()  # pop '?'
                first = stack.pop()
                stack.pop()  # pop ':'
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)


        return str(stack[-1])