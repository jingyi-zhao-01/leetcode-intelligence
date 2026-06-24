# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: row-with-maximum-ones
# source_path: LeetCode-Solutions-master/Python/row-with-maximum-ones.py
# solution_class: Solution
# submission_id: 6bdc833fc32caac48345fb604c21f83d49f8b2e0
# seed: 2905738703

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        return max(([i, mat[i].count(1)] for i in xrange(len(mat))), key=lambda x: x[1])