# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: regular-expression-matching
# source_path: LeetCode-Solutions-master/Python/regular-expression-matching.py
# solution_class: Solution4
# submission_id: ce537c0bd50889f809bfdffe501a54bd4bb600ad
# seed: 2125562521

# Time:  O(m * n)
# Space: O(n)

class Solution4(object):
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])