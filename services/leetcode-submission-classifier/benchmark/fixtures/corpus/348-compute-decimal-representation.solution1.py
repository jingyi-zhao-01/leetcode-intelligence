# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compute-decimal-representation
# source_path: LeetCode-Solutions-master/Python/compute-decimal-representation.py
# solution_class: Solution
# submission_id: b5be785205f60924ce4af880acbe54728ce19cc8
# seed: 1078202128

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        base = 1
        while n:
            n, r = divmod(n, 10)
            if r:
                result.append(r*base)
            base *= 10
        result.reverse()
        return result