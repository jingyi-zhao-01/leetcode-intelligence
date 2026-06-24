# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: game-of-life
# source_path: LeetCode-Solutions-master/Python/game-of-life.py
# solution_class: Solution
# submission_id: a6ccf914057ed72635efac00382544021039c31c
# seed: 109896249

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m else 0
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                ## Count live cells in 3x3 block.
                for I in xrange(max(i-1, 0), min(i+2, m)):
                    for J in xrange(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1

                # if (count == 4 && board[i][j]) means:
                #     Any live cell with three live neighbors lives.
                # if (count == 3) means:
                #     Any live cell with two live neighbors.
                #     Any dead cell with exactly three live neighbors lives.
                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 2  # Mark as live.

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1  # Update to the next state.