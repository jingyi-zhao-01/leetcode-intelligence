# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-largest-element-in-a-stream
# source_path: LeetCode-Solutions-master/Python/kth-largest-element-in-a-stream.py
# solution_class: Solution
# submission_id: 297ff7620da54b1c9ebd752947018bf34dec1ab7
# seed: 3254440583

# Time:  O(nlogk)
# Space: O(k)

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.__k = k
        self.__min_heap = []
        for n in nums:
            self.add(n)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.__min_heap, val)
        if len(self.__min_heap) > self.__k:
            heapq.heappop(self.__min_heap)
        return self.__min_heap[0]



