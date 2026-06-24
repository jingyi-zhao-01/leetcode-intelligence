# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenate-non-zero-digits-and-multiply-by-sum-i
# source_path: LeetCode-Solutions-master/Python/concatenate-non-zero-digits-and-multiply-by-sum-i.py
# solution_class: Solution
# submission_id: a453e695487c03e292462c533f896da482184fc4
# seed: 2152428064

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result

        total = x = 0
        while n:
            n, r = divmod(n, 10)
            total += r
            if r:
                x = x*10+r
        return reverse(x)*total