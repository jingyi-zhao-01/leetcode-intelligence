# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-similar-strings
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-similar-strings.py
# solution_class: Solution
# submission_id: e9ea1e39c629415385fb867a432180a9a8de0f01
# seed: 3626333941

# Time:  O(n * l)
# Space: O(n)

import collections
import itertools


# freq table, bitmask

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt = collections.Counter()
        result = 0
        for w in words:
            mask = reduce(lambda total, x: total|x, itertools.imap(lambda c: 1<<(ord(c)-ord('a')), w))
            result += cnt[mask]
            cnt[mask] += 1
        return result