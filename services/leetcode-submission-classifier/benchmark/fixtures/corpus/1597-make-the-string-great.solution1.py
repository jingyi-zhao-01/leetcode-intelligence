# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-the-string-great
# source_path: LeetCode-Solutions-master/Python/make-the-string-great.py
# solution_class: Solution
# submission_id: 0ed5986022aa950b4b4bc567d633a95785d29335
# seed: 1255596317

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        for ch in s:
            counter_ch = ch.upper() if ch.islower() else ch.lower()
            if stk and stk[-1] == counter_ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)