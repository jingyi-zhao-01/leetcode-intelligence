# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: arithmetic-slices
# source_path: LeetCode-Solutions-master/Python/arithmetic-slices.py
# solution_class: Solution
# submission_id: 658230805017c5a39e5454b2d877a00eeaff55ec
# seed: 2194984343

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, i = 0, 0
        while i+2 < len(A):
            start = i
            while i+2 < len(A) and A[i+2] + A[i] == 2*A[i+1]:
                res += i - start + 1
                i += 1
            i += 1

        return res