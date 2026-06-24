# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zigzag-iterator
# source_path: LeetCode-Solutions-master/Python/zigzag-iterator.py
# solution_class: Solution
# submission_id: 0351f7b4a49a6d6e2e704c2d64c6a8dbdc1851e5
# seed: 269946449

# Time:  O(n)
# Space: O(k)

import collections


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)


