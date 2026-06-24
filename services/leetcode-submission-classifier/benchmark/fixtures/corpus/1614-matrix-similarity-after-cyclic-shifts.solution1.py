# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: matrix-similarity-after-cyclic-shifts
# source_path: LeetCode-Solutions-master/Python/matrix-similarity-after-cyclic-shifts.py
# solution_class: Solution
# submission_id: 98d50b4b4b5298faa15c2daeb71ca165c1046149
# seed: 4213136356

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        return all(row[i] == row[(i+k)%len(row)]for row in mat for i in xrange(len(row)))