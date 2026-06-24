# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reconstruct-a-2-row-binary-matrix
# source_path: LeetCode-Solutions-master/Python/reconstruct-a-2-row-binary-matrix.py
# solution_class: Solution
# submission_id: 4bfaf365498c980c1e044b2622e80a3059e1f4fc
# seed: 2247336601

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        upper_matrix, lower_matrix = [0]*len(colsum), [0]*len(colsum)
        for i in xrange(len(colsum)):
            upper_matrix[i] = int(upper > 0 and colsum[i] != 0)
            lower_matrix[i] = colsum[i]-upper_matrix[i]
            upper -= upper_matrix[i]
            lower -= lower_matrix[i]
        return [upper_matrix, lower_matrix] if upper == lower == 0 else []