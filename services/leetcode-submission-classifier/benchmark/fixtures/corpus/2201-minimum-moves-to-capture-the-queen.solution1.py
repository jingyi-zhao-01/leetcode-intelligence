# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-capture-the-queen
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-capture-the-queen.py
# solution_class: Solution
# submission_id: afceea59b499f47440eb432c64054714d8030c10
# seed: 3428019549

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """
        if a == e and not (a == c and (b-d)*(f-d) < 0):
            return 1
        if b == f and not (b == d and (a-c)*(e-c) < 0):
            return 1
        if c+d == e+f and not (c+d == a+b and (c-a)*(e-a) < 0):
            return 1
        if c-d == e-f and not (c-d == a-b and (d-b)*(f-b) < 0):
            return 1
        return 2