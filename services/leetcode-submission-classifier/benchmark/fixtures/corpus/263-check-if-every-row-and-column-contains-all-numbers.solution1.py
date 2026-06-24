# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-every-row-and-column-contains-all-numbers
# source_path: LeetCode-Solutions-master/Python/check-if-every-row-and-column-contains-all-numbers.py
# solution_class: Solution
# submission_id: 7d6b45fb6b2afd7a2c561bc3a11d7894f3a28e87
# seed: 2346556275

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(len(set(row)) == len(matrix) for row in matrix) and all(len(set(matrix[i][j] for i in xrange(len(matrix)))) == len(matrix) for j in xrange(len(matrix[0])))