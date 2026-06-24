# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: short-encoding-of-words
# source_path: LeetCode-Solutions-master/Python/short-encoding-of-words.py
# solution_class: Solution
# submission_id: 090c1452b50214105310037b5ab7bb4e0946cf72
# seed: 639927807

# Time:  O(n), n is the total sum of the lengths of words
# Space: O(t), t is the number of nodes in trie

import collections
import functools

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words))
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()

        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)