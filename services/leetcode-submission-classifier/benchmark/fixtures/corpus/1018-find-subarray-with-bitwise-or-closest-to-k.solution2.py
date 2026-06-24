# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subarray-with-bitwise-or-closest-to-k
# source_path: LeetCode-Solutions-master/Python/find-subarray-with-bitwise-or-closest-to-k.py
# solution_class: Solution2
# submission_id: 81e39aba998ebcf05a5bfe0d90ab9840d232abc4
# seed: 3433680369

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# freq table, two pointers, sliding window, lc1521
class BitCount(object):
    def __init__(self, n):
        self.__l = 0
        self.__n = n
        self.__count = [0]*n
    
    def __iadd__(self, num):
        self.__l += 1
        base = 1
        for i in xrange(self.__n):
            if num&base:
                self.__count[i] += 1
            base <<= 1
        return self

    def __isub__(self, num):
        self.__l -= 1
        base = 1
        for i in xrange(self.__n):
            if num&base:
                self.__count[i] -= 1
            base <<= 1
        return self

    def bit_or(self):
        num, base = 0, 1
        for i in xrange(self.__n):
            if self.__count[i]:
                num |= base
            base <<= 1
        return num

                    

class Solution2(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, dp = float("inf"), set()  # at most O(logr) dp states
        for x in nums:
            dp = {x}|{f|x for f in dp}
            for f in dp:
                result = min(result, abs(f-k))
        return result