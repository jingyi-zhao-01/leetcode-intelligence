# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reaching-points
# source_path: LeetCode-Solutions-master/Python/reaching-points.py
# solution_class: Solution
# submission_id: 93bee4254dc6c7f7e37776d6cb1c7cdea612f8c9
# seed: 3220910682

# Time:  O(log(max(m, n)))
# Space: O(1)

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx < ty:
                sx, sy = sy, sx
                tx, ty = ty, tx
            if ty > sy:
                tx %= ty
            else:
                return (tx - sx) % ty == 0

        return False