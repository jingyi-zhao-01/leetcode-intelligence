# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-color-of-a-chessboard-square
# source_path: LeetCode-Solutions-master/Python/determine-color-of-a-chessboard-square.py
# solution_class: Solution
# submission_id: 73d3415cc043e0850bc795c29e2b4c4ccc9f209a
# seed: 481740942

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        return (ord(coordinates[0])-ord('a'))%2 != (ord(coordinates[1])-ord('1'))%2