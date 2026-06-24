# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-repair-cars
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-repair-cars.py
# solution_class: Solution
# submission_id: 6eabbcfbea0ee2b8ef466567a2876440417052ed
# seed: 4188417663

# Time:  O(mx * log(mn * c^2)) = O(mx * (logc + log(mn))), c = cars, mx = max(ranks), mn = min(ranks)
# Space: O(mx)

import collections


# freq table, binary search

class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def check(x):
            return sum(int((x//k)**0.5)*v for k, v in cnt.iteritems()) >= cars

        cnt = collections.Counter(ranks)
        left, right = 1, min(cnt.iterkeys())*cars**2
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left