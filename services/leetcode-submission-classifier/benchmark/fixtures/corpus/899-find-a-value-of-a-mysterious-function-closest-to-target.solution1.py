# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-a-value-of-a-mysterious-function-closest-to-target
# source_path: LeetCode-Solutions-master/Python/find-a-value-of-a-mysterious-function-closest-to-target.py
# solution_class: Solution
# submission_id: 163fb801ee029e9a8aaec094cff74701fc137957
# seed: 3446937119

# Time:  O(nlogm), m is the max value of arr
# Space: O(logm)

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
            
    def bit_and(self):
        num, base = 0, 1
        for i in xrange(self.__n):
            if self.__count[i] == self.__l:
                num |= base
            base <<= 1
        return num

class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        count = BitCount(max(arr).bit_length())
        result, left = float("inf"), 0
        for right in xrange(len(arr)):
            count += arr[right]
            while left <= right:
                f = count.bit_and()
                result = min(result, abs(f-target))
                if f >= target:
                    break
                count -= arr[left]
                left += 1
        return result