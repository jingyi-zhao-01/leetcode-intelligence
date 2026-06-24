# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-increasing-subsequence.py
# solution_class: Solution3
# submission_id: 4b9c722fa2f90e4641c109f469630d66cddde74e
# seed: 1160075254

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
    
        lookup = {x:i for i, x in enumerate(sorted(set(nums)))}
        bit = BIT(len(lookup), fn=max)
        for x in nums:
            bit.update(lookup[x], bit.query(lookup[x]-1)+1)
        return bit.query(len(lookup)-1)