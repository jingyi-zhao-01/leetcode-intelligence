# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: multiply-strings
# source_path: LeetCode-Solutions-master/Python/multiply-strings.py
# solution_class: Solution3
# submission_id: 1b10f624443b1c8ba5ab8e4cf53920478928ace6
# seed: 4287162290

# Time:  O(m * n)
# Space: O(m + n)

class Solution3(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))