# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alternating-digit-sum
# source_path: LeetCode-Solutions-master/Python/alternating-digit-sum.py
# solution_class: Solution
# submission_id: 4046ce5fc359ea68965ad076a45546573237696f
# seed: 1465665187

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        sign = 1
        while n:
            sign *= -1
            result += sign*(n%10)
            n //= 10
        return sign*result