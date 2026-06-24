# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subarray-with-bitwise-or-closest-to-k
# source_path: LeetCode-Solutions-master/Python/find-subarray-with-bitwise-or-closest-to-k.py
# solution_class: Solution
# submission_id: 70b683238109994c97673321a3d43ddb57fb3ee3
# seed: 577811777

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

                    

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = BitCount(max(nums).bit_length())
        result, left = float("inf"), 0
        for right in xrange(len(nums)):
            count += nums[right]
            while left <= right:
                f = count.bit_or()
                result = min(result, abs(f-k))
                if f <= k:
                    break
                count -= nums[left]
                left += 1
        return result