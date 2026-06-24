# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bold-words-in-string
# source_path: LeetCode-Solutions-master/Python/bold-words-in-string.py
# solution_class: Solution2
# submission_id: ba52096a3a6bd6fe8562ab8c57bbb4d77c099cd7
# seed: 1649594137

# Time:  O(n * l), n is the length of S, l is the average length of words
# Space: O(t)    , t is the size of trie

import collections
import functools

class Solution2(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        lookup = [0] * len(S)
        for d in words:
            pos = S.find(d)
            while pos != -1:
                lookup[pos:pos+len(d)] = [1] * len(d)
                pos = S.find(d, pos+1)

        result = []
        for i in xrange(len(S)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(S[i])
            if lookup[i] and (i == len(S)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)