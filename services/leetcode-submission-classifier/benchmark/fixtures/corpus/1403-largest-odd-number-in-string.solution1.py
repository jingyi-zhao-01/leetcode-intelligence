# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-odd-number-in-string
# source_path: LeetCode-Solutions-master/Python/largest-odd-number-in-string.py
# solution_class: Solution
# submission_id: fb3b292e271ac7016851b8fe113dcea7b01fccc6
# seed: 3135180538

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in reversed(xrange(len(num))):
            if int(num[i])%2:
                return num[:i+1]
        return ""