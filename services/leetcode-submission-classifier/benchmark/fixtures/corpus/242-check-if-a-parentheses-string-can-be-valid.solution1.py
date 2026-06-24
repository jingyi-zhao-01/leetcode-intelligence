# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-parentheses-string-can-be-valid
# source_path: LeetCode-Solutions-master/Python/check-if-a-parentheses-string-can-be-valid.py
# solution_class: Solution
# submission_id: 1a55ad509879940eb2be6a3a8a8844a9e89de008
# seed: 3357963475

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2:
            return False
        for direction, c in ((lambda x:x, '('), (reversed, ')')):
            cnt = bal = 0
            for i in direction(xrange(len(s))):
                if locked[i] == '0':
                    cnt += 1
                else:
                    bal += 1 if s[i] == c else -1
                    if cnt+bal < 0:
                        return False
        return True