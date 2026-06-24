# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: moving-average-from-data-stream
# source_path: LeetCode-Solutions-master/Python/moving-average-from-data-stream.py
# solution_class: Solution
# submission_id: 71daf0ab16df4ce47bba2f44c2c979ef4e0796ca
# seed: 3388276762

# Time:  O(1)
# Space: O(w)

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        return 1.0 * self.__sum / len(self.__q)



