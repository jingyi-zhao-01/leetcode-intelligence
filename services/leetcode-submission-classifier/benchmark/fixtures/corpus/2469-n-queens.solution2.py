# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-queens
# source_path: LeetCode-Solutions-master/Python/n-queens.py
# solution_class: Solution2
# submission_id: 8c66a5c59ac26b0c5f226fb8c5442796db7f96dd
# seed: 7858898

# Time:  O(n^2 * n!)
# Space: O(n)

class Solution2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row-col not in xy_diff and cur_row+col not in xy_sum:
                    dfs(col_per_row+[col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])
        ress = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in res] for res in ress]