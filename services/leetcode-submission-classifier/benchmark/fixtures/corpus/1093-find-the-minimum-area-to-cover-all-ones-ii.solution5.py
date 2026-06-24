# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-area-to-cover-all-ones-ii
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-area-to-cover-all-ones-ii.py
# solution_class: Solution5
# submission_id: 0128159dd3defa77c14dac7c7db2407572c72b55
# seed: 767363204

# Time:  O(max(n, m)^2)
# Space: O(max(n, m)^2)

# dp

class Solution5(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def minimumArea(min_i, max_i, min_j, max_j):
            def count(x1, y1, x2, y2):
                cnt = prefix[x2][y2]
                if x1-1 >= 0:
                    cnt -= prefix[x1-1][y2]
                if y1-1 >= 0:
                    cnt -= prefix[x2][y1-1]
                if x1-1 >= 0 and y1-1 >= 0:
                    cnt += prefix[x1-1][y1-1]
                return cnt

            min_r = binary_search(min_i, max_i, lambda i: count(min_i, min_j, i, max_j))
            max_r = binary_search_right(min_i, max_i, lambda i: count(i, min_j, max_i, max_j))
            min_c = binary_search(min_j, max_j, lambda j: count(min_i, min_j, max_i, j))
            max_c = binary_search_right(min_j, max_j, lambda j: count(min_i, j, max_i, max_j))
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for _ in xrange(4):
            prefix = [[0]*len(grid[0]) for _ in xrange(len(grid))]
            for i in xrange(len(grid)):
                for j in xrange(len(grid[0])):
                    prefix[i][j] = grid[i][j]
                    if i-1 >= 0:
                        prefix[i][j] += prefix[i-1][j]
                    if j-1 >= 0:
                        prefix[i][j] += prefix[i][j-1]
                    if i-1 >= 0 and j-1 >= 0:
                        prefix[i][j] -= prefix[i-1][j-1]
            for i in xrange(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in xrange(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in xrange(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in xrange(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = zip(*grid[::-1])
        return result