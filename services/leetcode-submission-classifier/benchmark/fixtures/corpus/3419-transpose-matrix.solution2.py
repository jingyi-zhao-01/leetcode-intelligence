# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transpose-matrix
# source_path: LeetCode-Solutions-master/Python/transpose-matrix.py
# solution_class: Solution2
# submission_id: d5a2b6a4619afb7fdf406023307719794059da28
# seed: 1707253447

# Time:  O(r * c)
# Space: O(1)

class Solution2(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)