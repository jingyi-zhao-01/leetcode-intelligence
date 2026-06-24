# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-flowers-in-full-bloom
# source_path: LeetCode-Solutions-master/Python/number-of-flowers-in-full-bloom.py
# solution_class: Solution
# submission_id: 0e0c983d082093728878db73077d714c102805fc
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
        cnt = collections.Counter()
        for s, e in flowers:
            cnt[s] += 1
            cnt[e+1] -= 1
        events = sorted(cnt.iterkeys())
        prefix = [0]
        for x in events:
            prefix.append(prefix[-1]+cnt[x])
        return [prefix[bisect.bisect_right(events, t)] for t in persons]