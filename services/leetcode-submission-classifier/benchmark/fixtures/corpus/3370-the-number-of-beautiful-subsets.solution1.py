# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-beautiful-subsets
# source_path: LeetCode-Solutions-master/Python/the-number-of-beautiful-subsets.py
# solution_class: Solution
# submission_id: a132ff55f3b22bb404b34c380761b0cf45bfa6ce
# seed: 3824999751

# Time:  O(n)
# Space: O(n)

import collections
import operator


# combinatorics, dp

class Solution(object):
    def beautifulSubsets(self, nums, k):
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
        return reduce(operator.mul, (count(i) for i in cnt.iterkeys() if i+k not in cnt))-1