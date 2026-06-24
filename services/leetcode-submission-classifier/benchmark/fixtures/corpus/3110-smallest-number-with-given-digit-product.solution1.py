# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-number-with-given-digit-product
# source_path: LeetCode-Solutions-master/Python/smallest-number-with-given-digit-product.py
# solution_class: Solution
# submission_id: cb88109617f0e2e00112236e3839dd570c8fd392
# seed: 301715039

# Time:  O(logn)
# Space: O(logn)

# greedy

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        for d in reversed(xrange(2, 9+1)):
            while n%d == 0:
                result.append(d)
                n //= d
        return "".join(map(str, reversed(result))) or "1" if n == 1 else "-1"