# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-flowers-in-full-bloom
# source_path: LeetCode-Solutions-master/Python/number-of-flowers-in-full-bloom.py
# solution_class: Solution
# submission_id: 1a792af5c8d01021fe8028715275a45cf4381092
# seed: 2681320696

# Time:  O(nlogn + mlogn)
# Space: O(n)

import bisect


# line sweep, binary search

class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        """
        :type flowers: List[List[int]]
        :type persons: List[int]
        :rtype: List[int]
        """
        starts, ends = [], []
        for s, e in flowers:
            starts.append(s)
            ends.append(e+1)
        starts.sort()
        ends.sort()
        return [bisect.bisect_right(starts, t)-bisect.bisect_right(ends, t) for t in persons]