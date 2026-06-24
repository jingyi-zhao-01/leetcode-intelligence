# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: squirrel-simulation
# source_path: LeetCode-Solutions-master/Python/squirrel-simulation.py
# solution_class: Solution
# submission_id: e1bff71105f5fbec123ebca0320ca13b00558347
# seed: 1617453425

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        result = 0
        d = float("inf")
        for nut in nuts:
            result += (distance(nut, tree) * 2)
            d = min(d, distance(nut, squirrel) - distance(nut, tree))
        return result + d