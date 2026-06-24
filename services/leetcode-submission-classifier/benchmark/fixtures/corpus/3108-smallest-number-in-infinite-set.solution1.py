# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-number-in-infinite-set
# source_path: LeetCode-Solutions-master/Python/smallest-number-in-infinite-set.py
# solution_class: Solution
# submission_id: 6ac237cd8644dbf3a588f79313b99e808f169593
# seed: 4109390892

# Time:  ctor:        O(1)
#        popSmallest: O(logn)
#        addBack:     O(logn)
# Space: O(n)

import heapq


# heap
class SmallestInfiniteSet(object):

    def __init__(self):
        self.__n = 1
        self.__lookup = set()
        self.__min_heap = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.__min_heap:
            result = heapq.heappop(self.__min_heap)
            self.__lookup.remove(result)
            return result
        result = self.__n
        self.__n += 1
        return result

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num >= self.__n or num in self.__lookup:
            return
        self.__lookup.add(num)
        heapq.heappush(self.__min_heap, num)
