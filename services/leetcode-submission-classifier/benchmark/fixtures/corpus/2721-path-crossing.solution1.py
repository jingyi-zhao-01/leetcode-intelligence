# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-crossing
# source_path: LeetCode-Solutions-master/Python/path-crossing.py
# solution_class: Solution
# submission_id: b7611d5b54464a1cce9a8889c044311c534c5904
# seed: 14661156

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x = y = 0
        lookup = {(0, 0)}
        for c in path:
            if c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            elif c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            if (x, y) in lookup:
                return True
            lookup.add((x, y))
        return False