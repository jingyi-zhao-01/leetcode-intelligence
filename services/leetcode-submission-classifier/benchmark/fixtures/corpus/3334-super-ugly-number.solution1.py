# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-ugly-number
# source_path: LeetCode-Solutions-master/Python/super-ugly-number.py
# solution_class: Solution
# submission_id: 6083f97f39e15fda6c8ddc704a606a420a79fc17
# seed: 626748800

# Time:  O(n * k)
# Space: O(n + k)

import heapq


# Heap solution. (620ms)

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap, uglies, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in xrange(1, n):
            uglies[i], k = heapq.heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]