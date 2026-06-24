# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-area-of-longest-diagonal-rectangle
# source_path: LeetCode-Solutions-master/Python/maximum-area-of-longest-diagonal-rectangle.py
# solution_class: Solution
# submission_id: bbc299239b08c5fda9a8f29960f5924609e61334
# seed: 3011067936

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        return max((l**2+w**2, l*w) for l, w in dimensions)[1]