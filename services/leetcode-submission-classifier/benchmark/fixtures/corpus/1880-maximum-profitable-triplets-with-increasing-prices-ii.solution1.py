# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profitable-triplets-with-increasing-prices-ii
# source_path: LeetCode-Solutions-master/Python/maximum-profitable-triplets-with-increasing-prices-ii.py
# solution_class: Solution
# submission_id: ab426282ef05355c20d2410e91d4c93aa420b2de
# seed: 3843725613

# Time:  O(nlogn)
# Space: O(n)

import itertools
from sortedcontainers import SortedList


# prefix sum, sorted list, binary search, mono stack

class Solution(object):
    def maxProfit(self, prices, profits):
        """
        :type prices: List[int]
        :type profits: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")
        def query(sl, k):
            j = sl.bisect_left((k,))
            return sl[j-1][1] if j-1 >= 0 else NEG_INF
    
        def update(sl, k, v):
            j = sl.bisect_left((k,))
            if j < len(sl) and sl[j][0] == k:
                if not (sl[j][1] < v):
                    return
                del sl[j]
            elif not (j-1 < 0 or sl[j-1][1] < v):
                return
            sl.add((k, v))
            while j+1 < len(sl) and sl[j+1][1] <= sl[j][1]:
                del sl[j+1]

        result = NEG_INF
        sl1, sl2 = SortedList(), SortedList()
        for price, profit in itertools.izip(prices, profits):
            result = max(result, query(sl2, price)+profit)
            update(sl1, price, profit)
            update(sl2, price, query(sl1, price)+profit)
        return result if result != NEG_INF else -1