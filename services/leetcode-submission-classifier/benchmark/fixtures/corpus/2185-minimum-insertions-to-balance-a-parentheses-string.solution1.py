# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-insertions-to-balance-a-parentheses-string
# source_path: LeetCode-Solutions-master/Python/minimum-insertions-to-balance-a-parentheses-string.py
# solution_class: Solution
# submission_id: ccf24472fac4274cb2a15c963d5ef52b2132e9f0
# seed: 1677525754

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        add, bal = 0, 0
        for c in s:
            if c == '(':
                if bal > 0 and bal%2:
                    add += 1
                    bal -= 1
                bal += 2
            else:
                bal -= 1
                if bal < 0:
                    add += 1
                    bal += 2
        return add + bal