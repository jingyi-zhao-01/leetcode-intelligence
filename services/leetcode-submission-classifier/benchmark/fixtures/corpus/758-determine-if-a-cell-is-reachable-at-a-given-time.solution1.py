# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-if-a-cell-is-reachable-at-a-given-time
# source_path: LeetCode-Solutions-master/Python/determine-if-a-cell-is-reachable-at-a-given-time.py
# solution_class: Solution
# submission_id: 47f75d6de45f708335c2373e26638208672f8266
# seed: 1695673518

# Time:  O(1)
# Space: O(1)

# constructive algorithms, math

class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        diff1, diff2 = abs(sx-fx), abs(sy-fy)
        mn = min(diff1, diff2)+abs(diff1-diff2)
        return t >= mn if mn else t != 1