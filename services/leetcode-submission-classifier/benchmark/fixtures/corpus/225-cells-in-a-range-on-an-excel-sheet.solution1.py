# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cells-in-a-range-on-an-excel-sheet
# source_path: LeetCode-Solutions-master/Python/cells-in-a-range-on-an-excel-sheet.py
# solution_class: Solution
# submission_id: cd9b7b6557681b58152ac16720577f44f2d62048
# seed: 1542673759

# Time:  O(26^2)
# Space: O(1)

# enumeration

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [chr(x)+chr(y) for x in xrange(ord(s[0]), ord(s[3])+1) for y in xrange(ord(s[1]), ord(s[4])+1)]