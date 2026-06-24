# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: seat-reservation-manager
# source_path: LeetCode-Solutions-master/Python/seat-reservation-manager.py
# solution_class: Solution
# submission_id: 36b5f80a805df64c73b7b4a003772cd4dccdb6b6
# seed: 1804857204

# Time:  ctor:      O(n)
#        reserve:   O(logn)
#        unreserve: O(logn)
# Space: O(n)

import heapq


class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__min_heap = range(1, n+1)
        # heapq.heapify(self.__min_heap)  # no need for sorted list

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.__min_heap)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.__min_heap, seatNumber)
