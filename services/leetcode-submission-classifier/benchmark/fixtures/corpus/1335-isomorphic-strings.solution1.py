# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: isomorphic-strings
# source_path: LeetCode-Solutions-master/Python/isomorphic-strings.py
# solution_class: Solution
# submission_id: 038056ee7180e8151d6f11f9989ecfab8ba4dd6c
# seed: 1941808198

# Time:  O(n)
# Space: O(1)

from itertools import izip  # Generator version of zip.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True