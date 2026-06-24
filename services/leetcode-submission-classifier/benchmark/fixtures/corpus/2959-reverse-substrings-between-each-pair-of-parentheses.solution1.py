# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-substrings-between-each-pair-of-parentheses
# source_path: LeetCode-Solutions-master/Python/reverse-substrings-between-each-pair-of-parentheses.py
# solution_class: Solution
# submission_id: 8c45e2ab3164c0f4270544704c0b92ec478a8564
# seed: 533583714

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk, lookup = [], {}
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                lookup[i], lookup[j] = j, i
        result = []
        i, d = 0, 1
        while i < len(s):
            if i in lookup:
                i = lookup[i]
                d *= -1
            else:
                result.append(s[i])
            i += d
        return "".join(result)