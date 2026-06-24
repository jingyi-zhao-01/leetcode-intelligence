# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: available-captures-for-rook
# source_path: LeetCode-Solutions-master/Python/available-captures-for-rook.py
# solution_class: Solution
# submission_id: acd5ab2640d960864fac59e8abdd4074382e93c8
# seed: 2457307726

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = None, None
        for i in xrange(8):
            if r is not None:
                break
            for j in xrange(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break

        result = 0
        for d in directions:
            nr, nc = r+d[0], c+d[1]
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'p':
                    result += 1
                if board[nr][nc] != '.':
                    break
                nr, nc= nr+d[0], nc+d[1]
        return result