# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: block-placement-queries
# source_path: LeetCode-Solutions-master/Python/block-placement-queries.py
# solution_class: Solution
# submission_id: dd1b048964dd8169960678632b6e9f7b44b8dd89
# seed: 3276360821

# Time:  O(qlogq)
# Space: O(q)

from sortedcontainers import SortedList


# sorted list, bit, fenwick tree

class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        class BIT(object):  # 0-indexed.
            def __init__(self, n, default=0, fn=lambda x, y: x+y):
                self.__bit = [default]*(n+1)  # Extra one for dummy node.
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
            
        sl = SortedList(q[1] for q in queries if q[0] == 1)
        val_to_idx = {x:i for i, x in enumerate(sl)}
        bit = BIT(len(val_to_idx), fn=max)
        for i in xrange(len(sl)):
            bit.update(val_to_idx[sl[i]], sl[i]-(sl[i-1] if i-1 >= 0 else 0))
        result = []
        for q in reversed(queries):
            i = sl.bisect_left(q[1])
            if q[0] == 1:
                if i+1 < len(sl):
                    bit.update(val_to_idx[sl[i+1]], sl[i+1]-(sl[i-1] if i-1 >= 0 else 0))
                del sl[i]
            else:
                result.append(q[1]-(sl[i-1] if i-1 >= 0 else 0) >= q[2] or (i-1 >= 0 and bit.query(val_to_idx[sl[i-1]]) >= q[2]))
        result.reverse()
        return result