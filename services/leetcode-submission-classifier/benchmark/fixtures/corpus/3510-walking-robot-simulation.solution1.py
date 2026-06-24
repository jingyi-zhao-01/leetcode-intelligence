# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: walking-robot-simulation
# source_path: LeetCode-Solutions-master/Python/walking-robot-simulation.py
# solution_class: Solution
# submission_id: 4929e47c56968f77eeec199c2b5ed15608726d98
# seed: 3638036441

# Time:  O(n + k)
# Space: O(k)

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, i = 0, 0, 0
        lookup = set(map(tuple, obstacles))
        result = 0
        for cmd in commands:
            if cmd == -2:
                i = (i-1) % 4
            elif cmd == -1:
                i = (i+1) % 4
            else:
                for k in xrange(cmd):
                    if (x+directions[i][0], y+directions[i][1]) not in lookup:
                        x += directions[i][0]
                        y += directions[i][1]
                        result = max(result, x*x + y*y)
        return result