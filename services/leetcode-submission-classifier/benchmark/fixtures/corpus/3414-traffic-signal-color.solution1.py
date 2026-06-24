# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: traffic-signal-color
# source_path: LeetCode-Solutions-master/Python/traffic-signal-color.py
# solution_class: Solution
# submission_id: 49fea782ce64ea64f47b9e41fbe37a1e9a681f99
# seed: 3989623641

# Time:  O(1)
# Space: O(1)

# simulation

class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        return "Invalid"