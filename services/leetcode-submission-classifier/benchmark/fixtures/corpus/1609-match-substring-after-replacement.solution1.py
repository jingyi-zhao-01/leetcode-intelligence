# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: match-substring-after-replacement
# source_path: LeetCode-Solutions-master/Python/match-substring-after-replacement.py
# solution_class: Solution
# submission_id: a248e164d9661e3e15aa76ceb847d5b5fe0a9fd8
# seed: 84595550

# Time:  O(n * k), n = len(s), k = len(sub)
# Space: O(m), m = len(mappings)

import collections


# brute force

class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        def transform(x):
            return ord(x)-ord('0') if x.isdigit() else ord(x)-ord('a')+10 if x.islower() else ord(x)-ord('A')+36

        def check(i):
            return all(sub[j] == s[i+j] or lookup[sub[j]][s[i+j]] for j in xrange(len(sub)))
            
        lookup = [[0]*62 for _ in xrange(62)]
        for a, b in mappings:
            lookup[transform(a)][transform(b)] = 1
        s = map(transform, s)
        sub = map(transform, sub)
        return any(check(i) for i in xrange(len(s)-len(sub)+1))