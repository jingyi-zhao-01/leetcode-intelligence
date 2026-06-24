# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reach-a-number
# source_path: LeetCode-Solutions-master/Python/reach-a-number.py
# solution_class: Solution
# submission_id: 960aa9cd4b6beed6132a6119b0fafd7597d1faaf
# seed: 3230904421

# Time:  O(logn)
# Space: O(1)

import math

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = int(math.ceil((-1+math.sqrt(1+8*target))/2))
        target -= k*(k+1)/2
        return k if target%2 == 0 else k+1+k%2