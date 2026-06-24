# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: harshad-number
# source_path: LeetCode-Solutions-master/Python/harshad-number.py
# solution_class: Solution
# submission_id: 90fc24760217247d393b98f0992efed24601a8c3
# seed: 2947230164

# Time:  O(logx)
# Space: O(1)

# math

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        y = x
        while y:
            y, r = divmod(y, 10)
            result += r
        return result if x%result == 0 else -1