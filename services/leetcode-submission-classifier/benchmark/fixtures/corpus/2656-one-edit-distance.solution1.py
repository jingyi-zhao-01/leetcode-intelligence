# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: one-edit-distance
# source_path: LeetCode-Solutions-master/Python/one-edit-distance.py
# solution_class: Solution
# submission_id: 74ecc4160609a846f83821f1eef8e05a0edc6cd0
# seed: 3095171402

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i += 1
        while i < m and s[i] == t[i + shift]:
            i += 1

        return i == m