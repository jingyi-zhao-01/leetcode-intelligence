# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-parenthesis-string
# source_path: LeetCode-Solutions-master/Python/valid-parenthesis-string.py
# solution_class: Solution
# submission_id: 43ef8d578f1cfc97387533e43e2202c2eb2df175
# seed: 2457894376

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower, upper = 0, 0  # keep lower bound and upper bound of '(' counts
        for c in s:
            lower += 1 if c == '(' else -1
            upper -= 1 if c == ')' else -1
            if upper < 0: break
            lower = max(lower, 0)
        return lower == 0  # range of '(' count is valid