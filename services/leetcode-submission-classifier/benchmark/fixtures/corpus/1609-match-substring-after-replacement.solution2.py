# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: match-substring-after-replacement
# source_path: LeetCode-Solutions-master/Python/match-substring-after-replacement.py
# solution_class: Solution2
# submission_id: bdb96721f07071f248ca5ddda485b44c299cb4da
# seed: 101513793

# Time:  O(n * k), n = len(s), k = len(sub)
# Space: O(m), m = len(mappings)

import collections


# brute force

class Solution2(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        def check(i):
            return all(sub[j] == s[i+j] or (sub[j], s[i+j]) in lookup for j in xrange(len(sub)))
            
        lookup = set()
        for a, b in mappings:
            lookup.add((a, b))
        return any(check(i) for i in xrange(len(s)-len(sub)+1))