# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-spaces-cleaning-robot-cleaned
# source_path: LeetCode-Solutions-master/Python/number-of-spaces-cleaning-robot-cleaned.py
# solution_class: Solution
# submission_id: 98bfd5a0c1d4abc5c8bb29a80a43420236874c94
# seed: 1669146905

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def numberOfCleanRooms(self, room):
        """
        :type room: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = r = c = d = 0
        while not room[r][c]&(1<<(d+1)):
            result += (room[r][c]>>1) == 0
            room[r][c] |= (1<<(d+1))
            dr, dc = directions[d]
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(room) and 0 <= nc < len(room[0]) and not (room[nr][nc]&1):
                r, c = nr, nc
            else:
                d = (d+1)%4
        return result