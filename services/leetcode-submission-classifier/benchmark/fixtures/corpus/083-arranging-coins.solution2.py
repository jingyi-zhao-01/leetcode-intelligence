# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: arranging-coins
# source_path: LeetCode-Solutions-master/Python/arranging-coins.py
# solution_class: Solution2
# submission_id: a044352d26f72ecf18f07222718c0cf045958c46
# seed: 3121577311

# Time:  O(logn)
# Space: O(1)

import math

class Solution2(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(mid, n):
            return mid*(mid+1) <= 2*n

        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid, n):
                right = mid-1
            else:
                left = mid+1
        return right