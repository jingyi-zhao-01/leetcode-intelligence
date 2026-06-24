# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-pair-with-different-frequencies
# source_path: LeetCode-Solutions-master/Python/smallest-pair-with-different-frequencies.py
# solution_class: Solution
# submission_id: 426232f4c8725c729b6bc2581092714a45774282
# seed: 3247111974

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def minDistinctFreqPair(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        INF = float("inf")
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        x = min(nums)
        mn = INF
        for y in nums:
            if cnt[y] != cnt[x]:
                mn = min(mn, y)
        return [x, mn] if mn is not INF else [-1, -1]