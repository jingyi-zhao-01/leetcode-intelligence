# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-even-number
# source_path: LeetCode-Solutions-master/Python/largest-even-number.py
# solution_class: Solution2
# submission_id: f953257f162aa06d27e82c35c578a9f8586282fe
# seed: 3942136283

# Time:  O(n)
# Space: O(1)

# math

class Solution2(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.rstrip('1')