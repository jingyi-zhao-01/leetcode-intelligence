# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fibonacci-number
# source_path: LeetCode-Solutions-master/Python/fibonacci-number.py
# solution_class: Solution2
# submission_id: 808fe57ec84a04375b98eab0137a2eca48c81a82
# seed: 4102525130

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in xrange(N):
            prev, current = current, prev + current,
        return prev