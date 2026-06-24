# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-distinct-integers-after-removing-zeros
# source_path: LeetCode-Solutions-master/Python/count-distinct-integers-after-removing-zeros.py
# solution_class: Solution
# submission_id: 48027d26d2a55745cfa61a0039eab922758186e5
# seed: 2242000426

# Time:  O(logn)
# Space: O(1)

# combinatorics

class Solution(object):
    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(n):
            result, base = 0, 1
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
                base *= 9
            return result, base

        m, base = reverse(n+1)
        result = (base-9)//(9-1)
        base //= 9
        while base:
            m, r = divmod(m, 10)
            if r == 0:
                break
            result += (r-1)*base
            base //= 9
        return result