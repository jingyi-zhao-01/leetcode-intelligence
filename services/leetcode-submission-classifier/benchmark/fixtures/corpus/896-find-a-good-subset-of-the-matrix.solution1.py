# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-a-good-subset-of-the-matrix
# source_path: LeetCode-Solutions-master/Python/find-a-good-subset-of-the-matrix.py
# solution_class: Solution
# submission_id: 665d1bd81f97c65cbc0e530eb2a5a6a9ac4baf0e
# seed: 3917719586

# Time:  O(m * 2^n)
# Space: O(2^n)

# bitmasks, constructive algorithms, greedy

class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        lookup = {}
        for i in xrange(len(grid)):
            mask = reduce(lambda mask, j: mask|(grid[i][j]<<j), xrange(len(grid[0])), 0)
            if not mask:
                return [i]
            for mask2, j in lookup.iteritems():
                if mask2&mask == 0:
                    return [j, i]
            lookup[mask] = i
        return []