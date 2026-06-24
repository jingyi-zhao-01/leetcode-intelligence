# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: preimage-size-of-factorial-zeroes-function
# source_path: LeetCode-Solutions-master/Python/preimage-size-of-factorial-zeroes-function.py
# solution_class: Solution
# submission_id: 81586cd2a94661125af61b62cc1daea6237835da
# seed: 4122510550

# Time:  O((logn)^2)
# Space: O(1)

class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def count_of_factorial_primes(n, p):
            cnt = 0
            while n > 0:
                cnt += n//p
                n //= p
            return cnt

        p = 5
        left, right = 0, p*K
        while left <= right:
            mid = left + (right-left)//2
            if count_of_factorial_primes(mid, p) >= K:
                right = mid-1
            else:
                left = mid+1
        return p if count_of_factorial_primes(left, p) == K else 0