# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strange-printer-ii
# source_path: LeetCode-Solutions-master/Python/strange-printer-ii.py
# solution_class: Solution
# submission_id: edbd3a2460ad56b14f48a8d94125af33569d7eeb
# seed: 3717588191

# Time:  O(c * m * n + e), c is the number of colors
#                        , e is the number of edges in adj, at most O(c^2)
# Space: O(e)

import collections

class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        VISITING, VISITED = range(2)
        def has_cycle(adj, color, lookup):
            stk = [(1, color)]
            while stk:
                step, color = stk.pop()
                if step == 1:
                    lookup[color] = VISITING
                    stk.append((2, color))
                    for new_color in adj[color]:
                        if new_color in lookup:
                            if lookup[new_color] == VISITED:
                                continue
                            return True  # VISITING
                        stk.append((1, new_color))
                elif step == 2:
                    lookup[color] = VISITED
            return False

        boxes = collections.defaultdict(lambda:[len(targetGrid), len(targetGrid[0]), -1, -1])
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                boxes[color][0] = min(boxes[color][0], r)
                boxes[color][1] = min(boxes[color][1], c)
                boxes[color][2] = max(boxes[color][2], r)
                boxes[color][3] = max(boxes[color][3], c)
        adj = collections.defaultdict(set)
        for color, (min_r, min_c, max_r, max_c) in boxes.iteritems():
            for r in xrange(min_r, max_r+1):
                for c in xrange(min_c, max_c+1):
                    if targetGrid[r][c] != color:
                        adj[color].add(targetGrid[r][c])

        lookup = {}
        return all(color in lookup or not has_cycle(adj, color, lookup) for color in boxes.iterkeys())