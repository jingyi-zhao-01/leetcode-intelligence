# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-it-is-a-straight-line
# source_path: LeetCode-Solutions-master/Python/check-if-it-is-a-straight-line.py
# solution_class: Solution
# submission_id: 6e6ac0cb19782eab498583798acd251fa482ef17
# seed: 2642676212

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        i, j = coordinates[:2]
        return all(i[0] * j[1] - j[0] * i[1] +
                   j[0] * k[1] - k[0] * j[1] +
                   k[0] * i[1] - i[0] * k[1] == 0
                   for k in coordinates)