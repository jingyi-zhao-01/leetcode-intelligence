# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-repair-cars
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-repair-cars.py
# solution_class: Solution2
# submission_id: 47a92624c29da1b3ce2866dd66c93f5d522106ee
# seed: 1361303303

# Time:  O(mx * log(mn * c^2)) = O(mx * (logc + log(mn))), c = cars, mx = max(ranks), mn = min(ranks)
# Space: O(mx)

import collections


# freq table, binary search

class Solution2(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        cnt = collections.Counter(ranks)
        min_heap = [(r*1**2, 1) for r in cnt.iterkeys()]
        heapq.heapify(min_heap)
        while cars > 0:
            t, k = heapq.heappop(min_heap)
            r = t//k**2
            cars -= cnt[r]
            k += 1
            heapq.heappush(min_heap, (r*k**2, k))
        return t