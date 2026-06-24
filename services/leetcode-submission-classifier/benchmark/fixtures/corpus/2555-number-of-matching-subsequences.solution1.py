# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-matching-subsequences
# source_path: LeetCode-Solutions-master/Python/number-of-matching-subsequences.py
# solution_class: Solution
# submission_id: 442b202f475c1198fad180197fac62bfa1a8c3a2
# seed: 2045133101

# Time:  O(n + w), n is the size of S, w is the size of words
# Space: O(k), k is the number of words

import collections

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it, None)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])