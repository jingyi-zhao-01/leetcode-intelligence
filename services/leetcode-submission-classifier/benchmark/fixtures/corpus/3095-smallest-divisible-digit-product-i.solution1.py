# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-divisible-digit-product-i
# source_path: LeetCode-Solutions-master/Python/smallest-divisible-digit-product-i.py
# solution_class: Solution
# submission_id: 8bbbb6535e704d60f37cff6ab677826881a6cc3e
# seed: 3468257276

# Time:  O(logn)
# Space: O(1)

# brute force

class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def check(x):
            result = 1
            while x:
                result = (result*(x%10))%t
                x //= 10
            return result == 0
    
        while not check(n):
            n += 1
        return n