# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-trailing-zeros-from-a-string
# source_path: LeetCode-Solutions-master/Python/remove-trailing-zeros-from-a-string.py
# solution_class: Solution
# submission_id: f05e979a53860b95e8465807639db4a35d4e2047
# seed: 2014488922

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        return num[:next(i for i in reversed(xrange(len(num))) if num[i] != '0')+1]