# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: climbing-stairs
# source_path: LeetCode-Solutions-master/Python/climbing-stairs.py
# solution_class: Solution2
# submission_id: ace3dcb7b5b21b8c817743624799c54f0d50294a
# seed: 142958496

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current,
        return current