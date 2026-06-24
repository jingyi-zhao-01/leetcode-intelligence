# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-ugly-number
# source_path: LeetCode-Solutions-master/Python/super-ugly-number.py
# solution_class: Solution2
# submission_id: f50cf7642c517aa41dcd4b46e12868dde10693e5
# seed: 3639233546

# Time:  O(n * k)
# Space: O(n + k)

import heapq


# Heap solution. (620ms)

class Solution2(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies, idx, heap, ugly_set = [0] * n, [0] * len(primes), [], set([1])
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))
            ugly_set.add(p)

        for i in xrange(1, n):
            uglies[i], k = heapq.heappop(heap)
            while (primes[k] * uglies[idx[k]]) in ugly_set:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))
            ugly_set.add(primes[k] * uglies[idx[k]])

        return uglies[-1]