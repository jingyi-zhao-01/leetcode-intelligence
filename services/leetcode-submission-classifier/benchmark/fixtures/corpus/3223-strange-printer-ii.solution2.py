# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strange-printer-ii
# source_path: LeetCode-Solutions-master/Python/strange-printer-ii.py
# solution_class: Solution2
# submission_id: 8334ad33c7a5d2fbdd8ba9f00a1f7e8ec2bc0fe8
# seed: 3341296930

# Time:  O(c * m * n + e), c is the number of colors
#                        , e is the number of edges in adj, at most O(c^2)
# Space: O(e)

import collections

class Solution2(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        VISITING, VISITED = range(2)
        def has_cycle(adj, color, lookup):
            lookup[color] = VISITING
            for new_color in adj[color]:
                if (new_color not in lookup and has_cycle(adj, new_color, lookup)) or \
                   lookup[new_color] == VISITING:
                    return True
            lookup[color] = VISITED
            return False          

        MAX_COLOR = 60
        adj = collections.defaultdict(set)
        for color in xrange(1, MAX_COLOR+1):
            min_r = len(targetGrid)
            min_c = len(targetGrid[0])
            max_r = -1
            max_c = -1
            for r in xrange(len(targetGrid)):
                for c in xrange(len(targetGrid[r])):
                    if targetGrid[r][c] == color:
                        min_r = min(min_r, r)
                        min_c = min(min_c, c)
                        max_r = max(max_r, r)
                        max_c = max(max_c, c)
            for r in xrange(min_r, max_r+1):
                for c in xrange(min_c, max_c+1):
                    if targetGrid[r][c] != color:
                        adj[color].add(targetGrid[r][c])

        lookup = {}
        return all(color in lookup or not has_cycle(adj, color, lookup) for color in xrange(1, MAX_COLOR+1))