# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 2-keys-keyboard
# source_path: LeetCode-Solutions-master/Python/2-keys-keyboard.py
# solution_class: Solution
# submission_id: 377dacb0a804dbc1d0d4f52c10b902180cc6af1e
# seed: 3337089359

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        p = 2
        # the answer is the sum of prime factors
        while p**2 <= n:
            while n % p == 0:
                result += p
                n //= p
            p += 1
        if n > 1:
            result += n
        return result