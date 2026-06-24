# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reordered-power-of-2
# source_path: LeetCode-Solutions-master/Python/reordered-power-of-2.py
# solution_class: Solution
# submission_id: b9b424d426308fc8e9d93e490f8bb217d0555b76
# seed: 2082275490

# Time:  O((logn)^2) = O(1) due to n is a 32-bit number
# Space: O(logn) = O(1)

import collections

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << i))
                   for i in xrange(31))