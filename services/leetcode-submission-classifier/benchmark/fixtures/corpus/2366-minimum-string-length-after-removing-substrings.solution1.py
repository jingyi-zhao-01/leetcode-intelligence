# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-string-length-after-removing-substrings
# source_path: LeetCode-Solutions-master/Python/minimum-string-length-after-removing-substrings.py
# solution_class: Solution
# submission_id: cda513f1cc48d4989654d00efa47e6447d3006e6
# seed: 2730079048

# Time:  O(n)
# Space: O(n)

# stack

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        for c in s:
            if stk and ((stk[-1] == 'A' and c == 'B') or (stk[-1] == 'C' and c == 'D')):
                stk.pop()
                continue
            stk.append(c)
        return len(stk)