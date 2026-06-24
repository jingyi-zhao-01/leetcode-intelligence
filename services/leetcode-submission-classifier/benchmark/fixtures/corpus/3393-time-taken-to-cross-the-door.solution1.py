# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-taken-to-cross-the-door
# source_path: LeetCode-Solutions-master/Python/time-taken-to-cross-the-door.py
# solution_class: Solution
# submission_id: 26ea25f9838b277a6fb192cccf12778cc0b51e1f
# seed: 360194802

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# queue, simulation

class Solution(object):
    def timeTaken(self, arrival, state):
        """
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        def go_until(t):
            while curr[0] <= t and any(q):
                if not q[direction[0]]:
                    direction[0] ^= 1
                result[q[direction[0]].popleft()] = curr[0]
                curr[0] += 1
    
        UNKNOWN, ENTERING, EXITING = range(-1, 1+1)
        result = [0]*len(arrival)
        curr, direction = [float("-inf")], [UNKNOWN]
        q = [collections.deque(), collections.deque()]
        for i, (a, s) in enumerate(itertools.izip(arrival, state)):
            go_until(a-1)
            q[s].append(i)
            if not (a <= curr[0]):
                curr, direction = [a], [EXITING]
        go_until(float("inf"))
        return result