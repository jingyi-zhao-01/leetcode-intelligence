# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-rand10-using-rand7
# source_path: LeetCode-Solutions-master/Python/implement-rand10-using-rand7.py
# solution_class: Solution
# submission_id: d273552803f2de2d54e5f968b3e5a729b2c26e7c
# seed: 1305240203

# Time:  O(1.189), counted by statistics, limit would be O(log10/log7) = O(1.183)
# Space: O(1)

import random


def rand7():
    return random.randint(1, 7)


# Reference: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C++JavaPython-Average-1.199-Call-rand7-Per-rand10

class Solution(object):
    def __init__(self):
        self.__cache = []

    def rand10(self):
        """
        :rtype: int
        """
        def generate(cache):
            n = 32
            curr = sum((rand7()-1) * (7**i) for i in xrange(n))
            rang = 7**n
            while curr < rang//10*10:
                cache.append(curr%10+1)
                curr /= 10
                rang /= 10

        while not self.__cache:
            generate(self.__cache)
        return self.__cache.pop()