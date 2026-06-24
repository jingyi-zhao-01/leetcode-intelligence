# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-completely-painted-row-or-column
# source_path: LeetCode-Solutions-master/Python/first-completely-painted-row-or-column.py
# solution_class: Solution
# submission_id: 734d75b9560ebb41609cc15d3549130efcb11e3a
# seed: 3227076981

# Time:  O(m * n)
# Space: O(m * n)

# hash table

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        lookup = {mat[i][j]: (i, j) for i in xrange(len(mat)) for j in xrange(len(mat[0]))}
        row = [0]*len(mat)
        col = [0]*len(mat[0])
        for idx, x in enumerate(arr):
            i, j = lookup[x]
            row[i] += 1
            col[j] += 1
            if row[i] == len(mat[0]) or col[j] == len(mat):
                return idx
        return -1