# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-a-value-of-a-mysterious-function-closest-to-target
# source_path: LeetCode-Solutions-master/Python/find-a-value-of-a-mysterious-function-closest-to-target.py
# solution_class: Solution2
# submission_id: 3637f9e587f254049b1819802f8caeb1ccb99b94
# seed: 3685783079

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

class Solution2(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        result, dp = float("inf"), set()  # at most O(logm) dp states
        for x in arr:
            dp = {x}|{f&x for f in dp}
            for f in dp:
                result = min(result, abs(f-target))
        return result