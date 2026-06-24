# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: right-triangles
# source_path: LeetCode-Solutions-master/Python/right-triangles.py
# solution_class: Solution3
# submission_id: e6f8a0cef25ab01261d502a2ded038cc6eeaa192
# seed: 2873115804

# Time:  O(n * m)
# Space: O(min(n, m))

# combinatorics

class Solution3(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get(i, j):
            return grid[i][j] if n < m else grid[j][i]

        def count(direction):
            result = 0
            cnt = [0]*min(n, m)
            for j in direction(xrange(max(n, m))):
                c = sum(get(i, j) for i in xrange(len(cnt)))
                for i in xrange(len(cnt)):
                    if get(i, j) == 0:
                        continue
                    result += cnt[i]
                    cnt[i] += c-1
            return result
        
        n, m = len(grid), len(grid[0])
        return count(lambda x: x)+count(reversed)