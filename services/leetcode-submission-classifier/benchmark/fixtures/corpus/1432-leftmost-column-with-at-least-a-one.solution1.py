# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: leftmost-column-with-at-least-a-one
# source_path: LeetCode-Solutions-master/Python/leftmost-column-with-at-least-a-one.py
# solution_class: Solution
# submission_id: d36375776c50eb10c9a060b5b92fb9afb3842041
# seed: 2500048363

# Time:  O(m + n)
# Space: O(1)

class BinaryMatrix(object):
    def get(self, row, col):
        pass

    def dimensions(self):
        pass

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        r, c = 0, n-1
        while r < m and c >= 0:
            if not binaryMatrix.get(r, c):
                r += 1
            else:
                c -= 1        
        return c+1 if c+1 != n else -1