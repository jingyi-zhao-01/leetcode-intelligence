# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-and-value-of-k
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-and-value-of-k.py
# solution_class: Solution
# submission_id: 2bb6d9fe442c7761a12b779303a25d2d95f05c39
# seed: 2109731024

# Time:  O(nlogr)
# Space: O(logr)

import collections


# dp, lc3171

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        dp = collections.defaultdict(int)
        for x in nums:
            new_dp = collections.defaultdict(int)
            if x&k == k:
                new_dp[x] += 1
                for y, c in dp.iteritems():
                    new_dp[y&x] += c
                if k in new_dp:
                    result += new_dp[k]                
            dp = new_dp
        return result