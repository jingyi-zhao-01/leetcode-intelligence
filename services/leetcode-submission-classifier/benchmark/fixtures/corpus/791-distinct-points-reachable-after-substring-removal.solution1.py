# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distinct-points-reachable-after-substring-removal
# source_path: LeetCode-Solutions-master/Python/distinct-points-reachable-after-substring-removal.py
# solution_class: Solution
# submission_id: 24569d528c8ac26c10308b36fdfde6eb80d2f441
# seed: 334263426

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def distinctPoints(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        DIRECTIONS = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
        x = y = 0
        lookup = {(x, y)}
        for i in xrange(k, len(s)):
            x += DIRECTIONS[s[i]][0]-DIRECTIONS[s[i-k]][0]
            y += DIRECTIONS[s[i]][1]-DIRECTIONS[s[i-k]][1]
            lookup.add((x, y))
        return len(lookup)