# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-unique-number
# source_path: LeetCode-Solutions-master/Python/first-unique-number.py
# solution_class: Solution
# submission_id: bb44389582bc9f71898896212bcb13d1fb394ddc
# seed: 4184124541

# Time:  ctor: O(k)
#        add: O(1)
#        showFirstUnique: O(1)
# Space: O(n)

import collections


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__q = collections.OrderedDict()
        self.__dup = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.__q:
            return next(iter(self.__q))
        return -1
    
    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.__dup and value not in self.__q:
            self.__q[value] = None
            return
        if value in self.__q:
            self.__q.pop(value)
            self.__dup.add(value)

