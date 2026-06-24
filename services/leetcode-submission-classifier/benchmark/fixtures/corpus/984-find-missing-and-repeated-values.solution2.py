# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-missing-and-repeated-values
# source_path: LeetCode-Solutions-master/Python/find-missing-and-repeated-values.py
# solution_class: Solution2
# submission_id: 776fffdad23dc1e3b5b11699f78fbf43287bbd29
# seed: 1854915108

# Time:  O(n^2)
# Space: O(1)

# bit manipulation

class Solution2(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        cnt = collections.Counter(x for row in grid for x in row)
        return [next(k for k, v in cnt.iteritems() if v == 2), next(x for x in xrange(1, len(grid)**2+1) if x not in cnt)]