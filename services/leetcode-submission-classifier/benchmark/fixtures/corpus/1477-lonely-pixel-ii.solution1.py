# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lonely-pixel-ii
# source_path: LeetCode-Solutions-master/Python/lonely-pixel-ii.py
# solution_class: Solution
# submission_id: 2ed4d89c5abbf686ae22fac6c799d983b3098a21
# seed: 3304980758

# Time:  O(m * n)
# Space: O(m * n)

import collections

class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        rows, cols = [0] * len(picture),  [0] * len(picture[0])
        lookup = collections.defaultdict(int)
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
            lookup[tuple(picture[i])] += 1

        result = 0
        for i in xrange(len(picture)):
            if rows[i] == N and lookup[tuple(picture[i])] == N:
                for j in xrange(len(picture[0])):
                     result += picture[i][j] == 'B' and cols[j] == N
        return result