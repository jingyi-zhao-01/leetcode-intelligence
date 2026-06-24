# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-transform-string
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-transform-string.py
# solution_class: Solution
# submission_id: bccb5b3dbf27ad5a1097dc9721e0b0072d15998d
# seed: 2835502024

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max((26-(ord(x)-ord('a')))%26 for x in s)