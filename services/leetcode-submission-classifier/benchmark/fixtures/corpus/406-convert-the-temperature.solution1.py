# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-the-temperature
# source_path: LeetCode-Solutions-master/Python/convert-the-temperature.py
# solution_class: Solution
# submission_id: 177301f05839c4f2f4cf48996002d50a5b923630
# seed: 1661943371

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius+273.15, celsius*1.80+32.00]