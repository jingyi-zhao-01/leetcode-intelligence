# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lonely-pixel-ii
# source_path: LeetCode-Solutions-master/Python/lonely-pixel-ii.py
# solution_class: Solution2
# submission_id: 67b27239f1bfa06d5b6d019943ce58274253740d
# seed: 1855494111

# Time:  O(m * n)
# Space: O(m * n)

import collections

class Solution2(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        lookup = collections.Counter(map(tuple, picture))
        cols = [col.count('B') for col in zip(*picture)]
        return sum(N * zip(row, cols).count(('B', N)) \
                   for row, cnt in lookup.iteritems() \
                   if cnt == N == row.count('B'))