# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: earliest-time-to-finish-one-task
# source_path: LeetCode-Solutions-master/Python/earliest-time-to-finish-one-task.py
# solution_class: Solution
# submission_id: f543cd624f604e1d0111d88b64f55f75fcd63279
# seed: 2947139092

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        return min(s+t for s, t in tasks)