# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: freedom-trail
# source_path: LeetCode-Solutions-master/Python/freedom-trail.py
# solution_class: Solution
# submission_id: bea2237d6c13fd75484c9d1eafe6f38c0d68fc8a
# seed: 3132372765

# Time:  O(k) ~ O(k * r^2)
# Space: O(r)

import collections

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        lookup = collections.defaultdict(list)
        for i in xrange(len(ring)):
            lookup[ring[i]].append(i)

        dp = [[0] * len(ring) for _ in xrange(2)]
        prev = [0]
        for i in xrange(1, len(key)+1):
            dp[i%2] = [float("inf")] * len(ring)
            for j in lookup[key[i-1]]:
                for k in prev:
                    dp[i%2][j] = min(dp[i%2][j],
                                     min((k+len(ring)-j) % len(ring), \
                                         (j+len(ring)-k) % len(ring)) + \
                                     dp[(i-1) % 2][k])
            prev = lookup[key[i-1]]
        return min(dp[len(key)%2]) + len(key)