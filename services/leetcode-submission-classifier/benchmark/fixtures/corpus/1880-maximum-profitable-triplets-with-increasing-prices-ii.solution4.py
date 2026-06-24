# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profitable-triplets-with-increasing-prices-ii
# source_path: LeetCode-Solutions-master/Python/maximum-profitable-triplets-with-increasing-prices-ii.py
# solution_class: Solution4
# submission_id: b00992dc8037276ba70edace3b0c88462de016df
# seed: 1373524137

# Time:  O(nlogn)
# Space: O(n)

import itertools
from sortedcontainers import SortedList


# prefix sum, sorted list, binary search, mono stack

class Solution4(object):
    def maxProfit(self, prices, profits):
        """
        :type prices: List[int]
        :type profits: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")
        # Range Maximum Query
        class SegmentTree(object):
            def __init__(self, N,
                         build_fn=lambda _: None,
                         query_fn=lambda x, y: max(x, y),
                         update_fn=lambda x, y: max(x, y)):
                self.tree = [None]*(2*2**((N-1).bit_length()))
                self.base = len(self.tree)//2
                self.query_fn = query_fn
                self.update_fn = update_fn
                for i in xrange(self.base, self.base+N):
                    self.tree[i] = build_fn(i-self.base)
                for i in reversed(xrange(1, self.base)):
                    self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

            def update(self, i, h):
                x = self.base+i
                self.tree[x] = self.update_fn(self.tree[x], h)
                while x > 1:
                    x //= 2
                    self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])

            def query(self, L, R):
                if L > R:
                    return None
                L += self.base
                R += self.base
                left = right = None
                while L <= R:
                    if L & 1:
                        left = self.query_fn(left, self.tree[L])
                        L += 1
                    if R & 1 == 0:
                        right = self.query_fn(self.tree[R], right)
                        R -= 1
                    L //= 2
                    R //= 2
                return self.query_fn(left, right)

        price_to_idx = {x:i for i, x in enumerate(sorted(set(prices)))}
        result = NEG_INF
        st1, st2 = SegmentTree(len(price_to_idx)), SegmentTree(len(price_to_idx))
        for price, profit in itertools.izip(prices, profits):
            mx2 = st2.query(0, price_to_idx[price]-1)
            if mx2 is not None:
                result = max(result, mx2+profit)
            st1.update(price_to_idx[price], profit)
            mx1 = st1.query(0, price_to_idx[price]-1)
            if mx1 is not None:
                st2.update(price_to_idx[price], mx1+profit)
        return result if result != NEG_INF else -1