# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fixed-point
# source_path: LeetCode-Solutions-master/Python/fixed-point.py
# solution_class: Solution
# submission_id: ab1777dbf6646d2f2364a911158260dd8203032e
# seed: 2531689332

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left <= right:
            mid = left + (right-left)//2
            if A[mid] >= mid:
                right = mid-1
            else:
                left = mid+1
        return left if A[left] == left else -1