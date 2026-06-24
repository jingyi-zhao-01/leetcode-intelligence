# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-hidden-sequences
# source_path: LeetCode-Solutions-master/Python/count-the-hidden-sequences.py
# solution_class: Solution
# submission_id: 81529006e54a0a3dde3077af66a34d4d3294998c
# seed: 2653463849

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        total = mn = mx = 0
        for x in differences:
            total += x
            mn = min(mn, total)
            mx = max(mx, total)
        return max((upper-lower)-(mx-mn)+1, 0)