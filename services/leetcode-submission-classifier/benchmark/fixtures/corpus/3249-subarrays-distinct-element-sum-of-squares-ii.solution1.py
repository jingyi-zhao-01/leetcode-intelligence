# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarrays-distinct-element-sum-of-squares-ii
# source_path: LeetCode-Solutions-master/Python/subarrays-distinct-element-sum-of-squares-ii.py
# solution_class: Solution
# submission_id: e4ff878ec68e51229433b01c6b8f52a92c512739
# seed: 3826867366

# Time:  O(nlogn)
# Space: O(n)

import collections
from sortedcontainers import SortedList


# bit, fenwick tree, sorted list, math

class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        class BIT(object):  # 0-indexed.
            def __init__(self, n):
                self.__bit = [0]*(n+1)  # Extra one for dummy node.

            def add(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] = (self.__bit[i]+val) % MOD
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = 0
                while i > 0:
                    ret = (ret+self.__bit[i]) % MOD
                    i -= (i & -i)
                return ret

        def update(accu, d):
            i = sl.bisect_left(idxs[x][-1])
            accu = (accu + d*(len(nums)*(2*len(sl)-1) - (2*i+1)*idxs[x][-1] - 2*(bit.query(len(nums)-1)-bit.query(idxs[x][-1])))) % MOD
            bit.add(idxs[x][-1], d*idxs[x][-1])
            return accu

        idxs = collections.defaultdict(list)
        for i in reversed(xrange(len(nums))):
            idxs[nums[i]].append(i)
        result = 0
        sl = SortedList(idxs[x][-1] for x in idxs)
        accu = (len(nums)*len(sl)**2) % MOD
        for i, x in enumerate(sl):
            accu = (accu-(2*i+1)*x) % MOD
        bit = BIT(len(nums))
        for x in sl:
            bit.add(x, x)
        for x in nums:
            result = (result+accu) % MOD  # accu = sum(count(i, k) for k in range(i, len(nums)))
            accu = update(accu, -1)
            del sl[0]
            idxs[x].pop()
            if not idxs[x]:
                continue
            sl.add(idxs[x][-1])
            accu = update(accu, +1)
        assert(accu == 0)
        return result