# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bulb-switcher
# source_path: LeetCode-Solutions-master/Python/bulb-switcher.py
# solution_class: Solution
# submission_id: 07477cec94774f0e60589377bf7acc09837f6383
# seed: 3932417867

# Time:  O(1)
# Space: O(1)

import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        type n: int
        rtype: int
        """
        # The number of full squares.
        return int(math.sqrt(n))