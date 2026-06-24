# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-even-number
# source_path: LeetCode-Solutions-master/Python/largest-even-number.py
# solution_class: Solution
# submission_id: f9900182213abdee7ed96622cf31beb47303e90f
# seed: 892725501

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        while result and result[-1] == '1':
            result.pop()
        return "".join(result)