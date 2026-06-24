# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-minimum-effort
# source_path: LeetCode-Solutions-master/Python/path-with-minimum-effort.py
# solution_class: Solution2
# submission_id: f9308665d20b0bc28641805aa7fa354eb7fb3c47
# seed: 137283806

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

import heapq


# Dijkstra algorithm solution

class Solution2(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        def index(n, i, j):
            return i*n + j
    
        diffs = []
        for i in xrange(len(heights)):
            for j in xrange(len(heights[0])):
                if i > 0:
                    diffs.append((abs(heights[i][j]-heights[i-1][j]), index(len(heights[0]), i-1, j), index(len(heights[0]), i, j)))
                if j > 0:
                    diffs.append((abs(heights[i][j]-heights[i][j-1]), index(len(heights[0]), i, j-1), index(len(heights[0]), i, j)))
        diffs.sort()
        union_find = UnionFind(len(heights)*len(heights[0]))
        for d, i, j in diffs:
            if union_find.union_set(i, j):
                if union_find.find_set(index(len(heights[0]), 0, 0)) == \
                   union_find.find_set(index(len(heights[0]), len(heights)-1, len(heights[0])-1)):
                    return d
        return 0