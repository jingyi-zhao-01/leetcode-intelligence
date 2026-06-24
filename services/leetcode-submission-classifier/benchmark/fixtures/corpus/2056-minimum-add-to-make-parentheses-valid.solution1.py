# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-add-to-make-parentheses-valid
# source_path: LeetCode-Solutions-master/Python/minimum-add-to-make-parentheses-valid.py
# solution_class: Solution
# submission_id: 885ef01a7ead2e073dd174f2a76f0341b017bba5
# seed: 1069302208

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        add, bal, = 0, 0
        for c in S:
            bal += 1 if c == '(' else -1
            if bal == -1:
                add += 1
                bal += 1
        return add + bal