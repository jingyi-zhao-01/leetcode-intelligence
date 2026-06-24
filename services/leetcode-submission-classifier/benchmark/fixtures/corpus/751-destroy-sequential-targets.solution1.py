# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: destroy-sequential-targets
# source_path: LeetCode-Solutions-master/Python/destroy-sequential-targets.py
# solution_class: Solution
# submission_id: 856ee3a3bb94fc2d2ed6c23e0f43892f48fb6019
# seed: 1152078630

# Time:  O(n)
# Space: O(s), s is the value of space

import collections


# freq table

class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        cnt = collections.Counter(x%space for x in nums)
        mx = max(cnt.itervalues())
        return min(x for x in nums if cnt[x%space] == mx)