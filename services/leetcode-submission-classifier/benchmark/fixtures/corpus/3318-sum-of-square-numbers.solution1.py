# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-square-numbers
# source_path: LeetCode-Solutions-master/Python/sum-of-square-numbers.py
# solution_class: Solution
# submission_id: 14f493e977079ab5f5e62119cbee0521b138866e
# seed: 2654958427

# Time:  O(sqrt(c) * logc)
# Space: O(1)

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in xrange(int(math.sqrt(c))+1):
            b = int(math.sqrt(c-a**2))
            if a**2 + b**2 == c:
                return True
        return False