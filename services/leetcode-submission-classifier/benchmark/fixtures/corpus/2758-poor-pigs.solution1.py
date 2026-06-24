# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: poor-pigs
# source_path: LeetCode-Solutions-master/Python/poor-pigs.py
# solution_class: Solution
# submission_id: 1f9f84384119bb9af565b13533939c125bd8eb7c
# seed: 2567106011

# Time:  O(1)
# Space: O(1)

import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return int(math.ceil(math.log(buckets) / math.log(minutesToTest / minutesToDie + 1)))