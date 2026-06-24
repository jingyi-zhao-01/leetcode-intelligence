# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-substrings-between-each-pair-of-parentheses
# source_path: LeetCode-Solutions-master/Python/reverse-substrings-between-each-pair-of-parentheses.py
# solution_class: Solution2
# submission_id: 0492694f6f2ce351b19ce9c23a60edd352d3479c
# seed: 194864468

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = [[]]
        for c in s:
            if c == '(':
                stk.append([])
            elif c == ')':
                end = stk.pop()
                end.reverse()
                stk[-1].extend(end)
            else:
                stk[-1].append(c)
        return "".join(stk.pop())