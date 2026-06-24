# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: egg-drop-with-2-eggs-and-n-floors
# source_path: LeetCode-Solutions-master/Python/egg-drop-with-2-eggs-and-n-floors.py
# solution_class: Solution
# submission_id: b855b4b6013702adeccc7117508d94d468ff5c82
# seed: 3470099225

# Time:  O(1)
# Space: O(1)

import math


# see the proof: https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/

class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.ceil((-1+(1+8*n)**0.5)/2))