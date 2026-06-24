# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-a-good-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-a-good-subsequence-ii.py
# solution_class: Solution2
# submission_id: 014a1459aee7af4864879a5dee329664202e1675
# seed: 2261608092

# Time:  O(n * k)
# Space: O(n * k)

import collections


# dp

class Solution2(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [collections.defaultdict(int) for _ in xrange(k+1)]
        result = [0]*(k+1)
        for x in nums:
            for i in reversed(xrange(k+1)):
                dp[i][x] = max(dp[i][x], result[i-1] if i-1 >= 0 else 0)+1
                result[i] = max(result[i], dp[i][x])
        return result[k]