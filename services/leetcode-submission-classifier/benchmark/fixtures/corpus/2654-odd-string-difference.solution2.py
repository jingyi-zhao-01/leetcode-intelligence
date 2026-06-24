# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: odd-string-difference
# source_path: LeetCode-Solutions-master/Python/odd-string-difference.py
# solution_class: Solution2
# submission_id: d87ab47fbb46c0f43c4c29913d1bd80f45db64c8
# seed: 165193448

# Time:  O(m * n), m is the number of words, n is the length of each word
# Space: O(1)

import collections


# freq table

class Solution2(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        cnt = collections.Counter(tuple(ord(w[i+1])-ord(w[i]) for i in xrange(len(w)-1)) for w in words)
        target = next(k for k, v in cnt.iteritems() if v == 1)
        return next(w for w in words if tuple(ord(w[i+1])-ord(w[i]) for i in xrange(len(w)-1)) == target)