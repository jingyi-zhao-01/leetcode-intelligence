# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtract-the-product-and-sum-of-digits-of-an-integer
# source_path: LeetCode-Solutions-master/Python/subtract-the-product-and-sum-of-digits-of-an-integer.py
# solution_class: Solution
# submission_id: ec63dddc627ed393ecb63413c78148d09a861e0e
# seed: 3194819402

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, total = 1, 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            total += r
        return product-total