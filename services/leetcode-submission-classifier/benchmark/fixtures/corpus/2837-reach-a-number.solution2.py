# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reach-a-number
# source_path: LeetCode-Solutions-master/Python/reach-a-number.py
# solution_class: Solution2
# submission_id: 0d27bbb109e52828780b2e981cc0f0ce7cfdc269
# seed: 755684218

# Time:  O(logn)
# Space: O(1)

import math

class Solution2(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target%2 == 0 else k+1+k%2