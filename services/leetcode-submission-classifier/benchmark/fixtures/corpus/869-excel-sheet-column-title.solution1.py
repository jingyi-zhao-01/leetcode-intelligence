# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: excel-sheet-column-title
# source_path: LeetCode-Solutions-master/Python/excel-sheet-column-title.py
# solution_class: Solution
# submission_id: 3dbf1aa05ec3f0aecd21d828ee0254139cd68d0f
# seed: 4049354018

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n:
            result += chr((n-1)%26 + ord('A'))
            n = (n-1)//26
        result.reverse()
        return "".join(result)