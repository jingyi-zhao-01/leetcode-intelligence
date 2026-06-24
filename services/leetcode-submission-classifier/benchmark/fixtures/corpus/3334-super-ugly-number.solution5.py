# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-ugly-number
# source_path: LeetCode-Solutions-master/Python/super-ugly-number.py
# solution_class: Solution5
# submission_id: 98ed658a4eae32ec5f609b574b2896017276d6f4
# seed: 1533870711

# Time:  O(n * k)
# Space: O(n + k)

import heapq


# Heap solution. (620ms)

class Solution5(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for p in primes:
            heapq.heappush(heap, p)
        for _ in xrange(n):
            ugly_number = heapq.heappop(heap)
            for i in xrange(len(primes)):
                if ugly_number % primes[i] == 0:
                    for j in xrange(i + 1):
                        heapq.heappush(heap, ugly_number * primes[j])
                    break

        return ugly_number