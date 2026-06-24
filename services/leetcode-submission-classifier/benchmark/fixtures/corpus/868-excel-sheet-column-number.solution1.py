# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: excel-sheet-column-number
# source_path: LeetCode-Solutions-master/Python/excel-sheet-column-number.py
# solution_class: Solution
# submission_id: 4d78b2743e68947a28389a9c2b487fb61820e86a
# seed: 876216823

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result