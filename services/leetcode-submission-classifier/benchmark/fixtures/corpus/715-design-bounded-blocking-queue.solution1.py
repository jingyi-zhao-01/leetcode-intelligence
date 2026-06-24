# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-bounded-blocking-queue
# source_path: LeetCode-Solutions-master/Python/design-bounded-blocking-queue.py
# solution_class: Solution
# submission_id: b8a90cb819a4961148a14bdea531ae2145367991
# seed: 2178866620

# Time:  O(n)
# Space: O(1)

import threading
import collections


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__cv = threading.Condition()
        self.__q = collections.deque()
        self.__cap = capacity

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        with self.__cv:
            while len(self.__q) == self.__cap:
                self.__cv.wait()
            self.__q.append(element)
            self.__cv.notifyAll()

    def dequeue(self):
        """
        :rtype: int
        """
        with self.__cv:
            while not self.__q:
                self.__cv.wait()
            self.__cv.notifyAll()
            return self.__q.popleft()

    def size(self):
        """
        :rtype: int
        """
        with self.__cv:
            return len(self.__q)
