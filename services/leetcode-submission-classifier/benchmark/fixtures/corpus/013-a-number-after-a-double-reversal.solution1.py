# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: a-number-after-a-double-reversal
# source_path: LeetCode-Solutions-master/Python/a-number-after-a-double-reversal.py
# solution_class: Solution
# submission_id: 024ae1a70551abe0cb4bb927ed650d40dbd6b939
# seed: 3012827902

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num%10