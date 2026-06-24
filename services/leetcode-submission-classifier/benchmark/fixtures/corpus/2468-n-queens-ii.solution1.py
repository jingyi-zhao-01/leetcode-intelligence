# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-queens-ii
# source_path: LeetCode-Solutions-master/Python/n-queens-ii.py
# solution_class: Solution
# submission_id: a2d90f12ebc32702ecd9bc048b120b3ba6405dc6
# seed: 1544160009

# Time:  O(n!)
# Space: O(n)

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(row):
            if row == n:
                return 1
            result = 0
            for i in xrange(n):
                if cols[i] or main_diag[row+i] or anti_diag[row-i+(n-1)]:
                    continue
                cols[i] = main_diag[row+i] = anti_diag[row-i+(n-1)] = True
                result += dfs(row+1)
                cols[i] = main_diag[row+i] = anti_diag[row-i+(n-1)] = False
            return result

        result = []
        cols, main_diag, anti_diag = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        return dfs(0)