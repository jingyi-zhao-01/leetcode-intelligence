# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-balloons
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-balloons.py
# solution_class: Solution
# submission_id: 3791d029218a1329496245c1b94e32d77ba02057
# seed: 4217022827

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        TARGET = "balloon"
        source_count = collections.Counter(text)
        target_count = collections.Counter(TARGET)
        return min(source_count[c]//target_count[c] for c in target_count.iterkeys())