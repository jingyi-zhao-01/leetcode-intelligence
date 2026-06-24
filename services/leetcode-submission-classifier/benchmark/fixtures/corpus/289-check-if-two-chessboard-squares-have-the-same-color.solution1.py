# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-two-chessboard-squares-have-the-same-color
# source_path: LeetCode-Solutions-master/Python/check-if-two-chessboard-squares-have-the-same-color.py
# solution_class: Solution
# submission_id: 4279abdd64ad63a51c908e983084c6b76ede3239
# seed: 2062019913

# Time:  O(1)
# Space: O(1)

# math, parity

class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        def parity(a):
            return reduce(lambda accu, x: (accu+x)%2, (ord(x) for x in a), 0)
        
        return parity(coordinate1) == parity(coordinate2)