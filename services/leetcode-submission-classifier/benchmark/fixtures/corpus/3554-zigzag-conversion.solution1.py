# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zigzag-conversion
# source_path: LeetCode-Solutions-master/Python/zigzag-conversion.py
# solution_class: Solution
# submission_id: bda4fd0ce154999ed0052cbf4eea0e56735ed6f1
# seed: 891860987

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step, zigzag = 2 * numRows - 2, ""
        for i in xrange(numRows):
            for j in xrange(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag