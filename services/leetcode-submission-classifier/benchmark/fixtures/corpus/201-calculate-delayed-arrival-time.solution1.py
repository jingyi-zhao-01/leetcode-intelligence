# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: calculate-delayed-arrival-time
# source_path: LeetCode-Solutions-master/Python/calculate-delayed-arrival-time.py
# solution_class: Solution
# submission_id: b5a6d9e2c7e36ce2f13f128bb0cb438e6e4d7d08
# seed: 3690169364

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        return (arrivalTime + delayedTime)%24