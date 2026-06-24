# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-achievable-number
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-achievable-number.py
# solution_class: Solution
# submission_id: 21a7f140c12f4b7f5dac76ef0f93c0cec80e1308
# seed: 3892458425

# Time:  O(1)
# Space: O(1)

# greedy

class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num+2*t