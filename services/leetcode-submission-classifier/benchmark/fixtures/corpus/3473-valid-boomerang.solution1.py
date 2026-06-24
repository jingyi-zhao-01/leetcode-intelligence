# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-boomerang
# source_path: LeetCode-Solutions-master/Python/valid-boomerang.py
# solution_class: Solution
# submission_id: 8f9d93fa81716294d55b508db98a474bd5a8e1c8
# seed: 2150672308

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) - \
               (points[0][0] - points[2][0]) * (points[0][1] - points[1][1]) != 0