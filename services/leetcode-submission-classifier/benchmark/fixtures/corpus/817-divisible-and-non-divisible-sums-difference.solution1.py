# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisible-and-non-divisible-sums-difference
# source_path: LeetCode-Solutions-master/Python/divisible-and-non-divisible-sums-difference.py
# solution_class: Solution
# submission_id: ae64e3277a82d693d733706c18f7b8c78071613a
# seed: 3990110641

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def arithmetic_progression_sum(a, d, l):
            return (a+(a+(l-1)*d))*l//2
    
        return arithmetic_progression_sum(1, 1, n) - 2*arithmetic_progression_sum(m, m, n//m)