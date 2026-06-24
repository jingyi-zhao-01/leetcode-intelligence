# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-bold-tag-in-string
# source_path: LeetCode-Solutions-master/Python/add-bold-tag-in-string.py
# solution_class: Solution2
# submission_id: 0019dbbf5c4bae52d88a2e2f0361b6258c4e4b3b
# seed: 2288196651

# Time:  O(n * d * l), l is the average string length
# Space: O(n)

import collections
import functools


# 59ms

class Solution2(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(s)
        for i in xrange(len(s)):
            curr = trie
            k = -1
            for j in xrange(i, len(s)):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "_end" in curr:
                    k = j
            for j in xrange(i, k+1):
                lookup[j] = True

        result = []
        for i in xrange(len(s)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)