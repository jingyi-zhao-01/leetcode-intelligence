# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-convert-time
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-convert-time.py
# solution_class: Solution
# submission_id: 8e2c5d1d35c9c317bbbabb48b953c2ecaa628fd2
# seed: 3492910385

# Time:  O(1)
# Space: O(1)

# greedy

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        OPS = (60, 15, 5, 1)
        diff = (int(correct[:2])*60+int(correct[3:]))-(int(current[:2])*60+int(current[3:]))
        result = 0
        for x in OPS:
            q, diff = divmod(diff, x)
            result += q
        return result