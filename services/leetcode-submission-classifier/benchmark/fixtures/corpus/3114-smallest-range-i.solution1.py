# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-range-i
# source_path: LeetCode-Solutions-master/Python/smallest-range-i.py
# solution_class: Solution
# submission_id: 9237089f837ded960d4e075c874a0abd684d0c2c
# seed: 1191381265

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)