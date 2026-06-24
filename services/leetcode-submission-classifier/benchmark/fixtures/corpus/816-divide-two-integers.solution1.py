# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-two-integers
# source_path: LeetCode-Solutions-master/Python/divide-two-integers.py
# solution_class: Solution
# submission_id: 2678e57a22e1c8bcae54ca9f6a1d00c12a8aed14
# seed: 4222853346

# Time:  O(logn) = O(1)
# Space: O(1)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            return -result
        else:
            return result

    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)