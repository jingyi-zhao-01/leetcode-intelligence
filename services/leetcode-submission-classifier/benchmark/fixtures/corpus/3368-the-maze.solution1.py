# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-maze
# source_path: LeetCode-Solutions-master/Python/the-maze.py
# solution_class: Solution
# submission_id: 5398ae101551f8e313d53a76b443f3b9b61de314
# seed: 2016952353

# Time:  O(max(r, c) * w)
# Space: O(w)

import collections

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def neighbors(maze, node):
            for i, j in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                x, y = node
                while 0 <= x + i < len(maze) and \
                      0 <= y + j < len(maze[0]) and \
                      not maze[x+i][y+j]:
                    x += i
                    y += j
                yield x, y

        start, destination = tuple(start), tuple(destination)
        queue = collections.deque([start])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited: continue
            if node == destination:
                return True
            visited.add(node)
            for neighbor in neighbors(maze, node):
                queue.append(neighbor)

        return False