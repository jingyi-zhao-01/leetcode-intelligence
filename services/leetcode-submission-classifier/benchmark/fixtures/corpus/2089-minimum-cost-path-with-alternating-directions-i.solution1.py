# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-path-with-alternating-directions-i
# source_path: LeetCode-Solutions-master/Python/minimum-cost-path-with-alternating-directions-i.py
# solution_class: Solution
# submission_id: a2e3ffbbed1a0f44d3d65bcc421c7d844761add6
# seed: 3088391450

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def minCost(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m, n) == (1, 1):
            return 1
        if (m, n) in ((1, 2), (2, 1)):
            return 3
        return -1