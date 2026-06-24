# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shift-2d-grid
# source_path: LeetCode-Solutions-master/Python/shift-2d-grid.py
# solution_class: Solution
# submission_id: 6c8f6b4a83a04f81b66e4e4f214e6093f0440664
# seed: 164626674

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def rotate(grids, k):
            def reverse(grid, start, end):
                while start < end:
                    start_r, start_c = divmod(start, len(grid[0]))
                    end_r, end_c = divmod(end-1, len(grid[0]))
                    grid[start_r][start_c], grid[end_r][end_c] = grid[end_r][end_c], grid[start_r][start_c]
                    start += 1
                    end -= 1

            k %= len(grid)*len(grid[0])
            reverse(grid, 0, len(grid)*len(grid[0]))
            reverse(grid, 0, k)
            reverse(grid, k, len(grid)*len(grid[0]))

        rotate(grid, k)
        return grid