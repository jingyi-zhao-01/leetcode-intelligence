# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-ugly-number
# source_path: LeetCode-Solutions-master/Python/super-ugly-number.py
# solution_class: Solution4
# submission_id: fe677647e7d33ee985b976be6c13f25ce89b7657
# seed: 4090752529

# Time:  O(n * k)
# Space: O(n + k)

import heapq


# Heap solution. (620ms)

class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in xrange(1, n):
            uglies[i] = min(ugly_by_prime)
            for k in xrange(len(primes)):
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]

        return uglies[-1]