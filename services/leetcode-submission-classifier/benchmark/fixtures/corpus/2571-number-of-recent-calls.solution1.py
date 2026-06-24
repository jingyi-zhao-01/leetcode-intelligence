# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-recent-calls
# source_path: LeetCode-Solutions-master/Python/number-of-recent-calls.py
# solution_class: Solution
# submission_id: ceebfaf6a45b58045410f6fe3d6d7dc652ff9552
# seed: 2706002687

# Time:  O(1) on average
# Space: O(w), w means the size of the last milliseconds.

import collections


class RecentCounter(object):

    def __init__(self):
        self.__q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.__q.append(t)
        while self.__q[0] < t-3000:
            self.__q.popleft()
        return len(self.__q)
