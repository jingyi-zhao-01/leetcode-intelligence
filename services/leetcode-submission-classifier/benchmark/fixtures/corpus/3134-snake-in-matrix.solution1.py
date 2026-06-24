# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: snake-in-matrix
# source_path: LeetCode-Solutions-master/Python/snake-in-matrix.py
# solution_class: Solution
# submission_id: 04ed290389a7b944bc5a722a008d5f3de692d038
# seed: 3890039743

# Time:  O(c)
# Space: O(1)

# simulation

class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        lookup = {"UP":(-1, 0), "RIGHT":(0, 1), "DOWN":(1, 0), "LEFT":(0, -1)}
        r = c = 0
        for x in commands:
            dr, dc = lookup[x]
            r, c = r+dr, c+dc
        return r*n+c