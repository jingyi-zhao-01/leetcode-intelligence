# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-primes-between-number-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/sum-of-primes-between-number-and-its-reverse.py
# solution_class: Solution
# submission_id: a2b67ebfc49f192fd724c97d454bc2a0f2aef564
# seed: 1991935040

# Time:  precompute: O(r)
#        runtime:    O(1)
# Space: O(r)

# number theory, prefix sum
def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
    primes = []
    spf = [-1]*(n+1)  # the smallest prime factor
    for i in xrange(2, n+1):
        if spf[i] == -1:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > n or p > spf[i]:
                break
            spf[i*p] = p
    return spf

def precompute(n):
    spf = linear_sieve_of_eratosthenes(n)
    prefix = [0]*(len(spf)+1)
    for i in xrange(len(prefix)-1):
        prefix[i+1] = prefix[i]+(i if spf[i] == i else 0)
    return prefix


MAX_N = 1000
PREFIX = precompute(MAX_N)

class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result
        
        left, right = n, reverse(n)
        if left > right:
            left, right = right, left
        return PREFIX[right+1]-PREFIX[left]