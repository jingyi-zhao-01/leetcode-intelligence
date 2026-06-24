# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lonely-pixel-i
# source_path: LeetCode-Solutions-master/Python/lonely-pixel-i.py
# solution_class: Solution
# submission_id: 78f08d13e76f31437f059f45a6aff52ceaf97b9d
# seed: 274659502

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows, cols = [0] * len(picture),  [0] * len(picture[0])
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        result = 0
        for i in xrange(len(picture)):
            if rows[i] == 1:
                for j in xrange(len(picture[0])):
                     result += picture[i][j] == 'B' and cols[j] == 1
        return result