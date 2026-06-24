# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: is-subsequence
# source_path: LeetCode-Solutions-master/Python/is-subsequence.py
# solution_class: Solution
# submission_id: 3b397e42d2dab208d8a0fb87e23adc3f93d6f942
# seed: 1055784924

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
                break
        return i == len(s)