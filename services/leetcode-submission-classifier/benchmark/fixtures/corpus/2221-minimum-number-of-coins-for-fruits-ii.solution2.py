# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-coins-for-fruits-ii
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-coins-for-fruits-ii.py
# solution_class: Solution2
# submission_id: acfcbe5819eb2360b818df6b39bb607f197a75dd
# seed: 1337465651

# Time:  O(n)
# Space: O(n)

import collections


# dp, mono deque

class Solution2(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [float("inf")]*(len(prices)+1)
        dp[0] = 0
        sl = SortedList()
        j = 0
        for i in xrange(len(prices)):
            sl.add((dp[i]+prices[i], i))
            while j+(j+1) < i:
                sl.remove(((dp[j]+prices[j], j)))
                j += 1
            dp[i+1] = sl[0][0]
        return dp[-1]