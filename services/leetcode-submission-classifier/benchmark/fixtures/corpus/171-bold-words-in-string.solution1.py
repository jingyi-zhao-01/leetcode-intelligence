# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bold-words-in-string
# source_path: LeetCode-Solutions-master/Python/bold-words-in-string.py
# solution_class: Solution
# submission_id: 24894684252d21b331dadfeb9fc117f2c5dd659d
# seed: 1832160571

# Time:  O(n * l), n is the length of S, l is the average length of words
# Space: O(t)    , t is the size of trie

import collections
import functools

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(S)
        for i in xrange(len(S)):
            curr = trie
            k = -1
            for j in xrange(i, len(S)):
                if S[j] not in curr:
                    break
                curr = curr[S[j]]
                if "_end" in curr:
                    k = j
            for j in xrange(i, k+1):
                lookup[j] = True

        result = []
        for i in xrange(len(S)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(S[i])
            if lookup[i] and (i == len(S)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)