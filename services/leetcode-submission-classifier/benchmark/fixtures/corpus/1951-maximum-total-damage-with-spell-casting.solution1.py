# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-damage-with-spell-casting
# source_path: LeetCode-Solutions-master/Python/maximum-total-damage-with-spell-casting.py
# solution_class: Solution
# submission_id: 72bc5814188e6806231b31eb78068a29e3e66dc4
# seed: 2361600318

# Time:  O(nlogn)
# Space: O(1)

import collections


# sort, dp, two pointers, sliding window, deque

class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        DIST = 2
        power.sort()
        dp = collections.deque()
        mx = 0
        for x in power:
            if dp and dp[-1][0] == x:
                dp[-1][1] += x
                continue
            while dp and dp[0][0]+DIST < x:
                mx = max(mx, dp.popleft()[1])
            dp.append([x, mx+x])
        return max(x for _, x in dp)