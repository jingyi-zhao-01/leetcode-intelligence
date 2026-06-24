# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-trapezoids-i
# source_path: LeetCode-Solutions-master/Python/count-number-of-trapezoids-i.py
# solution_class: Solution
# submission_id: 188bf89fbcaf996b390525951b2370ddeb3a2381
# seed: 2737276302

# Time:  O(n)
# Space: O(n)

import collections


# freq table, combinatorics

class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        cnt = collections.defaultdict(int)
        for _, y in points:
            cnt[y] += 1
        result = total = 0
        for c in cnt.itervalues():
            curr = (c*(c-1)//2)%MOD
            result = (result+(total*curr)%MOD)%MOD
            total = (total+curr)%MOD
        return result