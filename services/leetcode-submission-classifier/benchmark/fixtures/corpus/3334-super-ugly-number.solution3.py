# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-ugly-number
# source_path: LeetCode-Solutions-master/Python/super-ugly-number.py
# solution_class: Solution3
# submission_id: beecabe77d123c1053e133924f7c3792aa861463
# seed: 2068757034

# Time:  O(n * k)
# Space: O(n + k)

import heapq


# Heap solution. (620ms)

class Solution3(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies, idx, heap = [1], [0] * len(primes), []
        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in xrange(1, n):
            min_val, k = heap[0]
            uglies += [min_val]

            while heap[0][0] == min_val:  # worst time: O(klogk)
                min_val, k = heapq.heappop(heap)
                idx[k] += 1
                heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]