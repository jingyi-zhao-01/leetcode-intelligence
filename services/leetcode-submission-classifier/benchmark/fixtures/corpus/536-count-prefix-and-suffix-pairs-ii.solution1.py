# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-prefix-and-suffix-pairs-ii
# source_path: LeetCode-Solutions-master/Python/count-prefix-and-suffix-pairs-ii.py
# solution_class: Solution
# submission_id: 5ef7c465d4ed71effb026d0cd86e04c293cd75b5
# seed: 2659218818

# Time:  O(n * l)
# Space: O(t)

import collections


# trie

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for w in words:
            curr = trie
            for i in xrange(len(w)):
                curr = curr[w[i], w[~i]]
                result += curr["_cnt"] if "_cnt" in curr else 0
            curr["_cnt"] = curr["_cnt"]+1 if "_cnt" in curr else 1
        return result