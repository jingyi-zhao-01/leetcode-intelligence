# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: angle-between-hands-of-a-clock
# source_path: LeetCode-Solutions-master/Python/angle-between-hands-of-a-clock.py
# solution_class: Solution
# submission_id: aa9caf6722d54e353cc8f47e385887c4de74e8c9
# seed: 558540326

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle1 = (hour % 12 * 60.0 + minutes) / 720.0
        angle2 = minutes / 60.0
        diff = abs(angle1-angle2)
        return min(diff, 1.0-diff) * 360.0