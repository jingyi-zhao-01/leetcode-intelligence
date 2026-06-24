# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: complete-prime-number
# source_path: LeetCode-Solutions-master/Python/complete-prime-number.py
# solution_class: Solution
# submission_id: 1a10b1d6335c3c836eec3cca3fd71e9ec339d9ad
# seed: 867764156

# Time:  O(logn * sqrt(n))
# Space: O(1)

# prefix sum, number theory

class Solution(object):
    def completePrime(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def is_prime(n):
            if (n <= 1) or (n != 2 and n%2 == 0):
                return False
            for i in xrange(3, n+1, 2):
                if i*i > n:
                    break
                if n%i == 0:
                    return False
            return True

        suffix, base = 0, 1
        while num:
            if not is_prime(num):
                return False
            suffix += (num%10)*base
            if not is_prime(suffix):
                return False
            num //= 10
            base *= 10
        return True