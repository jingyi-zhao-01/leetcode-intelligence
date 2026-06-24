# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-steps-to-make-two-strings-anagram-ii
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-steps-to-make-two-strings-anagram-ii.py
# solution_class: Solution
# submission_id: 3f5569a2b910fdd0cbed55c0d674df8d557d746e
# seed: 842565303

# Time:  O(n)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cnt1, cnt2 = collections.Counter(s), collections.Counter(t)
        return sum((cnt1-cnt2).itervalues())+sum((cnt2-cnt1).itervalues())