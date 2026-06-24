# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-digit-one
# source_path: LeetCode-Solutions-master/Python/number-of-digit-one.py
# solution_class: Solution
# submission_id: 6311f64624522de498458be17020e85105bc37bf
# seed: 3948192861

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        DIGIT = 1
        is_zero = int(DIGIT == 0)
        result = is_zero
        base = 1
        while n >= base:
            result += (n//(10*base)-is_zero)*base + \
                      min(base, max(n%(10*base) - DIGIT*base + 1, 0))
            base *= 10
        return result