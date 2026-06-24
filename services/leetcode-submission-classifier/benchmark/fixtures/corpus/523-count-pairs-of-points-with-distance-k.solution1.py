# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-points-with-distance-k
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-points-with-distance-k.py
# solution_class: Solution
# submission_id: 232f08f0bf1e08fd220479a0735bf2df0f1a2432
# seed: 2228345448

# Time:  O(n * k)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for x, y in coordinates:
            for i in xrange(k+1):
                result += cnt.get((x^i, y^(k-i)), 0)
            cnt[(x, y)] += 1
        return result