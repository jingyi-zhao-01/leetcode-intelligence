# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-balanced-subsequence-sum
# source_path: LeetCode-Solutions-master/Python/maximum-balanced-subsequence-sum.py
# solution_class: Solution2
# submission_id: c40f3fcd890a3060e0b65a071e72803e3114340e
# seed: 3256408349

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list, binary search, mono stack

class Solution2(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        :type nums: List[int]
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

        val_to_idx = {x:i for i, x in enumerate(sorted({x-i for i, x in enumerate(nums)}))}
        bit = BIT(len(val_to_idx), default=NEG_INF, fn=max)
        for i, x in enumerate(nums):
            v = max(bit.query(val_to_idx[x-i]), 0)+x
            bit.update(val_to_idx[x-i], v)
        return bit.query(len(val_to_idx)-1)