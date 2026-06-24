# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-1d-array-into-2d-array
# source_path: LeetCode-Solutions-master/Python/convert-1d-array-into-2d-array.py
# solution_class: Solution
# submission_id: 721cf0d120c792ea50f513c303f4dd6beb244110
# seed: 504614327

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [original[i:i+n] for i in xrange(0, len(original), n)] if len(original) == m*n else []