# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nearest-exit-from-entrance-in-maze
# source_path: LeetCode-Solutions-master/Python/nearest-exit-from-entrance-in-maze.py
# solution_class: Solution
# submission_id: 25908d49c0b62d77ac0ed6acd70b8c28a384b3c9
# seed: 2007237858

# Time:  O(m * n)
# Space: O(m + n)

# bi-bfs solution

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = ' '
        entrance = tuple(entrance)
        left = set([entrance])
        right = set([(r, 0) for r in xrange(len(maze)-1) if maze[r][0] == '.' and (r, 0) != entrance] +
                    [(len(maze)-1, c) for c in xrange(len(maze[0])-1) if maze[len(maze)-1][c] == '.' and (len(maze)-1, c) != entrance] +
                    [(r, len(maze[0])-1) for r in reversed(xrange(1, len(maze))) if maze[r][len(maze[0])-1] == '.' and (r, len(maze[0])-1) != entrance] +
                    [(0, c) for c in reversed(xrange(1, len(maze[0]))) if maze[0][c] == '.' and (0, c) != entrance])
        steps = 0
        while left:
            for (r, c) in left:
                maze[r][c] = visited
            new_left = set()
            for (r, c) in left:
                if (r, c) in right: 
                    return steps
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(maze) and
                            0 <= nc < len(maze[0]) and
                            maze[nr][nc] == '.'):
                        continue
                    new_left.add((nr, nc))
            left = new_left
            steps += 1
            if len(left) > len(right): 
                left, right = right, left
        return -1