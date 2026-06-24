# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-non-decreasing-or-non-increasing
# source_path: LeetCode-Solutions-master/Python/make-array-non-decreasing-or-non-increasing.py
# solution_class: Solution2
# submission_id: bedf21b5224778459d8f49dfe46aa68da088bef4
# seed: 1120110834

# Time:  O(nlogn)
# Space: O(n)

import heapq


# greedy, heap

class Solution2(object):
    def convertArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = sorted(set(nums))
        def f(nums):
            dp = collections.defaultdict(int)  # dp[i]: min(cnt(j) for j in vals if j <= i)
            for x in nums:
                prev = -1
                for i in vals:
                    dp[i] = min(dp[i]+abs(i-x), dp[prev]) if prev != -1 else dp[i]+abs(i-x)
                    prev = i
            return dp[vals[-1]]

        return min(f(nums), f((x for x in reversed(nums))))