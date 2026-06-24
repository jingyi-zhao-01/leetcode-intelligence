# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-coins-for-fruits
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-coins-for-fruits.py
# solution_class: Solution
# submission_id: 66d263664153d47ee2983d9ee37ab646e5a8a0a1
# seed: 2384762692

# Time:  O(n)
# Space: O(n)

import collections


# dp, mono deque

class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [float("inf")]*(len(prices)+1)
        dp[0] = 0
        dq = collections.deque()
        j = 0
        for i in xrange(len(prices)):
            while dq and dp[dq[-1]]+prices[dq[-1]] >= dp[i]+prices[i]:
                dq.pop()
            dq.append(i)
            while j+(j+1) < i:
                assert(len(dq) != 0)
                if dq[0] == j:
                    dq.popleft()
                j += 1
            dp[i+1] = dp[dq[0]]+prices[dq[0]]
        return dp[-1]