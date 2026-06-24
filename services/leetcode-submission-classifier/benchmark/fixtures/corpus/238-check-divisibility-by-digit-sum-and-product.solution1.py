# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-divisibility-by-digit-sum-and-product
# source_path: LeetCode-Solutions-master/Python/check-divisibility-by-digit-sum-and-product.py
# solution_class: Solution
# submission_id: 81717f4c266c87c3849eedc65dda08b4926c0072
# seed: 3792297082

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curr = n
        total, product = 0, 1
        while curr:
            curr, r = divmod(curr, 10)
            total += r
            product *= r
        return n%(total+product) == 0