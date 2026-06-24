# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-k-free-subsets
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-k-free-subsets.py
# solution_class: Solution
# submission_id: dd3604953ef55477cf32824a12792f151b80cf37
# seed: 657013792

# Time:  O(n)
# Space: O(n)

import collections
import operator


# combinatorics, dp

class Solution(object):
    def countTheNumOfKFreeSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(x):
            y = x
            while y-k in cnt:
                y -= k
            dp = [1, 0]  # dp[0]: count without i, dp[1]: count with i
            for i in xrange(y, x+1, k):
                dp = [dp[0]+dp[1], dp[0]*((1<<cnt[i])-1)]
            return sum(dp)

        cnt = collections.Counter(nums)
        return reduce(operator.mul, (count(i) for i in cnt.iterkeys() if i+k not in cnt))