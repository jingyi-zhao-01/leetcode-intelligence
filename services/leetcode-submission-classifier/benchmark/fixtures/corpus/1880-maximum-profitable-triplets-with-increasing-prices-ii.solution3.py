# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profitable-triplets-with-increasing-prices-ii
# source_path: LeetCode-Solutions-master/Python/maximum-profitable-triplets-with-increasing-prices-ii.py
# solution_class: Solution3
# submission_id: a1d9c063175428d5237e29c5af67402508cadffe
# seed: 2076935903

# Time:  O(nlogn)
# Space: O(n)

import itertools
from sortedcontainers import SortedList


# prefix sum, sorted list, binary search, mono stack

class Solution3(object):
    def maxProfit(self, prices, profits):
        """
        :type prices: List[int]
        :type profits: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")
        class BIT(object):  # 0-indexed.
            def __init__(self, n, default=0, fn=lambda x, y: x+y):
                self.__bit = [NEG_INF]*(n+1)  # Extra one for dummy node.
                self.__default = default
                self.__fn = fn

            def update(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] = self.__fn(self.__bit[i], val)
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = self.__default
                while i > 0:
                    ret = self.__fn(ret, self.__bit[i])
                    i -= (i & -i)
                return ret

        price_to_idx = {x:i for i, x in enumerate(sorted(set(prices)))}
        result = NEG_INF
        bit1, bit2 = BIT(len(price_to_idx), default=NEG_INF, fn=max), BIT(len(price_to_idx), default=NEG_INF, fn=max)
        for price, profit in itertools.izip(prices, profits):
            result = max(result, bit2.query(price_to_idx[price]-1)+profit)
            bit1.update(price_to_idx[price], profit)
            bit2.update(price_to_idx[price], bit1.query(price_to_idx[price]-1)+profit)
        return result if result != NEG_INF else -1