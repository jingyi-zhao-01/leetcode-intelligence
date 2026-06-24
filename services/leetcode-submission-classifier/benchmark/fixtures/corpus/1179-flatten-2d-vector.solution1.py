# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flatten-2d-vector
# source_path: LeetCode-Solutions-master/Python/flatten-2d-vector.py
# solution_class: Solution
# submission_id: 0af3af0f65436744f9525d9c93beb059d04c968c
# seed: 194548205

# Time:  O(1)
# Space: O(1)

from collections import deque


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.stack = deque((len(v), iter(v)) for v in vec2d if v)

    def next(self):
        """
        :rtype: int
        """
        length, iterator = self.stack.popleft()
        if length > 1:
            self.stack.appendleft((length-1, iterator))
        return next(iterator)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)
