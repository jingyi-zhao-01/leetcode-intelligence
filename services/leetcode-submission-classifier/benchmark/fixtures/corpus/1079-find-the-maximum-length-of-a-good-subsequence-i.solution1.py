# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-a-good-subsequence-i
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-a-good-subsequence-i.py
# solution_class: Solution
# submission_id: b44102a5311e2638c88010823327af6418459a2b
# seed: 2603628334

# Time:  O(n * k)
# Space: O(n * k)

import collections


# dp

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = {x:i for i, x in enumerate(set(nums))}
        dp = [[0]*len(lookup) for _ in xrange(k+1)]
        result = [0]*(k+1)
        for x in nums:
            x = lookup[x]
            for i in reversed(xrange(k+1)):
                dp[i][x] = max(dp[i][x], result[i-1] if i-1 >= 0 else 0)+1
                result[i] = max(result[i], dp[i][x])
        return result[k]