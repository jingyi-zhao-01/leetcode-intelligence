# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-number-of-elements-in-subset
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-number-of-elements-in-subset.py
# solution_class: Solution
# submission_id: 27e2a88163c7ab9883b5b396f4ba8cb43cc412e6
# seed: 3283191212

# Time:  O(n)
# Space: O(n)

import collections


# freq table, dp

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        dp = {}
        result = 0
        for x in cnt.iterkeys():
            if x == 1:
                result = max(result, cnt[x]-(1 if cnt[x]%2 == 0 else 0))
                continue
            stk = []
            while x not in dp and x in cnt and cnt[x] >= 2:
                stk.append(x)
                x *= x
            if x not in dp:
                if x not in cnt:
                    x = stk.pop()
                dp[x] = 1
            l = dp[x]
            while stk:
                l += 2
                dp[stk.pop()] = l
            result = max(result, l)
        return result 