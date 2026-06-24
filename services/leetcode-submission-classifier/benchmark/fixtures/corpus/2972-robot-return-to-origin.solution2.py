# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: robot-return-to-origin
# source_path: LeetCode-Solutions-master/Python/robot-return-to-origin.py
# solution_class: Solution
# submission_id: 83d73462add04ffde476f5c55af150acdaeb173f
# seed: 2365879567

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v, h = 0, 0
        for move in moves:
            if move == 'U':
                v += 1
            elif move == 'D':
                v -= 1
            elif move == 'R':
                h += 1
            elif move == 'L':
                h -= 1
        return v == 0 and h == 0