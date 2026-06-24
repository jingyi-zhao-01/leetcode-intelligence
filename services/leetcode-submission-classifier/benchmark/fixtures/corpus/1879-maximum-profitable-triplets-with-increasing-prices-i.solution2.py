# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profitable-triplets-with-increasing-prices-i
# source_path: LeetCode-Solutions-master/Python/maximum-profitable-triplets-with-increasing-prices-i.py
# solution_class: Solution2
# submission_id: cd68fcdd422ffb0907eadc505ede2af0a103d8d5
# seed: 4180573265

# Time:  O(nlogn)
# Space: O(n)

import itertools
from sortedcontainers import SortedList


# prefix sum, sorted list, binary search, mono stack

class Solution2(object):
    def maxProfit(self, prices, profits):
        """
        :type prices: List[int]
        :type profits: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")

        right = [NEG_INF]*len(prices)
        sl = SortedList()
        for i in reversed(xrange(len(prices))):
            j = sl.bisect_left((-prices[i],))
            if j-1 >= 0:
                right[i] = sl[j-1][1]
            if not (j-1 < 0 or sl[j-1][1] < profits[i]):
                continue
            sl.add((-prices[i], profits[i]))
            j = sl.bisect_left((-prices[i], profits[i]))
            while j+1 < len(sl) and sl[j+1][1] <= sl[j][1]:
                del sl[j+1]
        result = NEG_INF
        sl = SortedList()
        for i in xrange(len(prices)):
            j = sl.bisect_left((prices[i],))
            if j-1 >= 0:
                result = max(result, sl[j-1][1]+profits[i]+right[i])
            if not (j-1 < 0 or sl[j-1][1] < profits[i]):
                continue
            sl.add((prices[i], profits[i]))
            j = sl.bisect_left((prices[i], profits[i]))
            while j+1 < len(sl) and sl[j+1][1] <= sl[j][1]:
                del sl[j+1]
        return result if result != NEG_INF else -1