# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-keypresses
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-keypresses.py
# solution_class: Solution
# submission_id: e6fbba908ec6808d3f27613910d69a74a2d05b91
# seed: 3919559875

# Time:  O(n)
# Space: O(1)

import collections


# greedy, sort

class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(cnt*(i//9+1) for i, cnt in enumerate(sorted(collections.Counter(s).itervalues(), reverse=True)))