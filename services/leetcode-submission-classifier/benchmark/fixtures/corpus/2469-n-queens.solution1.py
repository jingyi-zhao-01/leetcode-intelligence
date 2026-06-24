# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-queens
# source_path: LeetCode-Solutions-master/Python/n-queens.py
# solution_class: Solution
# submission_id: dce193f1ed8a037e3067e0a1996d3ad2a60586d4
# seed: 2306739036

# Time:  O(n^2 * n!)
# Space: O(n)

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(row):
            if row == n:
                result.append(map(lambda x: '.'*x + "Q" + '.'*(n-x-1), curr))
                return
            for i in xrange(n):
                if cols[i] or main_diag[row+i] or anti_diag[row-i+(n-1)]:
                    continue
                cols[i] = main_diag[row+i] = anti_diag[row-i+(n-1)] = True
                curr.append(i)
                dfs(row+1)
                curr.pop()
                cols[i] = main_diag[row+i] = anti_diag[row-i+(n-1)] = False

        result, curr = [], []
        cols, main_diag, anti_diag = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        dfs(0)
        return result