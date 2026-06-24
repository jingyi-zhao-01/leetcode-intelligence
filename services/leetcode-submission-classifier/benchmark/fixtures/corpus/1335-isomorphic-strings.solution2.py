# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: isomorphic-strings
# source_path: LeetCode-Solutions-master/Python/isomorphic-strings.py
# solution_class: Solution2
# submission_id: 7017a3121b9c414e4ee0239a41880e68b11053ec
# seed: 2037866338

# Time:  O(n)
# Space: O(1)

from itertools import izip  # Generator version of zip.

class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True