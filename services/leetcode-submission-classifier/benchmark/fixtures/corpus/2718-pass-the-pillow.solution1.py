# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pass-the-pillow
# source_path: LeetCode-Solutions-master/Python/pass-the-pillow.py
# solution_class: Solution
# submission_id: 4fb24ce23dc467ed69912fea475a38aca77825d7
# seed: 2456832168

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        return n-abs((n-1)-(time%(2*(n-1))))