# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-special-quadruplets
# source_path: LeetCode-Solutions-master/Python/count-special-quadruplets.py
# solution_class: Solution2
# submission_id: ba8fe6b127df904d4b20cb9b78f4e04500baf35c
# seed: 545398263

# Time:  O(n^3)
# Space: O(n)

import collections

class Solution2(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = collections.defaultdict(list)
        for d in xrange(3, len(nums)):
            for c in xrange(2, d):
                lookup[nums[d]-nums[c]].append(c)
        return sum(sum(b < c for c in lookup[nums[a]+nums[b]]) for b in xrange(1, len(nums)-2) for a in xrange(b))