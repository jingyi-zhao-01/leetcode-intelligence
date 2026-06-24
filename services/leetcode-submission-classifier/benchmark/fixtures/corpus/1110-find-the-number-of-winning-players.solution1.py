# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-winning-players
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-winning-players.py
# solution_class: Solution
# submission_id: 9930f18ae33cfa43c7b051b6baf25cb57c3a7542
# seed: 69698343

# Time:  O(p), p = len(pick)
# Space: O(min(n * c, p)), c = max(y)

import collections


# freq table

class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        cnts = collections.defaultdict(lambda: collections.defaultdict(int))
        for x, y in pick:
            cnts[x][y] += 1
        return sum(i < max(cnt.itervalues()) for i, cnt in cnts.iteritems())