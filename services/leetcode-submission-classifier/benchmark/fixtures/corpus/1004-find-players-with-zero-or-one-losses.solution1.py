# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-players-with-zero-or-one-losses
# source_path: LeetCode-Solutions-master/Python/find-players-with-zero-or-one-losses.py
# solution_class: Solution
# submission_id: 95d30349ff426e73bf0a5c4fc82cae1fcfa290ac
# seed: 1598408581

# Time:  O(nlogn)
# Space: O(n)

import collections


# hash, sort

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lose = collections.defaultdict(int)
        players_set = set()
        for x, y in matches:
            lose[y] += 1
            players_set.add(x)
            players_set.add(y)
        return [[x for x in sorted(players_set) if lose[x] == i] for i in xrange(2)]