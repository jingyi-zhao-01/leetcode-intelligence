# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-th-tribonacci-number
# source_path: LeetCode-Solutions-master/Python/n-th-tribonacci-number.py
# solution_class: Solution2
# submission_id: ae8705268ef33654eeebd4583058a73ef0390456
# seed: 3103826717

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 0, 1, 1
        for _ in xrange(n):
            a, b, c = b, c, a+b+c
        return a