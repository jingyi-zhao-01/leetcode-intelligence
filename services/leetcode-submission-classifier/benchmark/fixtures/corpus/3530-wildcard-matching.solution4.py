# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wildcard-matching
# source_path: LeetCode-Solutions-master/Python/wildcard-matching.py
# solution_class: Solution4
# submission_id: dd85b1b6f59ff6a96972b04d967888d25572b13c
# seed: 3083546275

# Time:  O(m + n) ~ O(m * n)
# Space: O(1)

# iterative solution with greedy

class Solution4(object):
    # @return a boolean
    def isMatch(self, s, p):
        if not p or not s:
            return not s and not p

        if p[0] != '*':
            if p[0] == s[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0:
                if self.isMatch(s, p[1:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[1:])