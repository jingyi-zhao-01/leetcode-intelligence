# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-pow
# source_path: LeetCode-Solutions-master/Python/super-pow.py
# solution_class: Solution
# submission_id: 15ae777ec447cd4b82019ce392f388ae922d1bea
# seed: 1184891107

# Time:  O(n), n is the size of b.
# Space: O(1)

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def myPow(a, n, b):
            result = 1
            x = a % b
            while n:
                if n & 1:
                    result = result * x % b
                n >>= 1
                x = x * x % b
            return result % b

        result = 1
        for digit in b:
            result = myPow(result, 10, 1337) * myPow(a, digit, 1337) % 1337
        return result