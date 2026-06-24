# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-string-length-after-balanced-removals
# source_path: LeetCode-Solutions-master/Python/minimum-string-length-after-balanced-removals.py
# solution_class: Solution
# submission_id: 60c6be6efc22858992237a499036fbcd3509bbf2
# seed: 3155320640

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        return abs(s.count('a')-s.count('b'))