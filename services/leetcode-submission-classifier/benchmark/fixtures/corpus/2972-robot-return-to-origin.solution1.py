# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: robot-return-to-origin
# source_path: LeetCode-Solutions-master/Python/robot-return-to-origin.py
# solution_class: Solution
# submission_id: 3bcb318738e5dbcc1000d4611cc8ec679f0cf205
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
        count = collections.Counter(moves)
        return count['L'] == count['R'] and count['U'] == count['D']