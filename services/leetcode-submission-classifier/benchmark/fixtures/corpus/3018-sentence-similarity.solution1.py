# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sentence-similarity
# source_path: LeetCode-Solutions-master/Python/sentence-similarity.py
# solution_class: Solution
# submission_id: bd0ce73e04b4151a8389063fa50d22b144d4f2f2
# seed: 1076821105

# Time:  O(n + p)
# Space: O(p)

import itertools

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        lookup = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in lookup or (w2, w1) in lookup \
                   for w1, w2 in itertools.izip(words1, words2))