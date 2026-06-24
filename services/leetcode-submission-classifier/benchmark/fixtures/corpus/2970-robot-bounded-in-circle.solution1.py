# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: robot-bounded-in-circle
# source_path: LeetCode-Solutions-master/Python/robot-bounded-in-circle.py
# solution_class: Solution
# submission_id: d5f8e707460071517efa0824bd4e0a8465ec312b
# seed: 3656169998

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [[ 1, 0], [0, -1], [-1, 0], [0, 1]]
        x, y, i = 0, 0, 0
        for instruction in instructions:
            if instruction == 'R':
                i = (i+1) % 4
            elif instruction == 'L':
                i = (i-1) % 4
            else:
                x += directions[i][0]
                y += directions[i][1]
        return (x == 0 and y == 0) or i > 0