# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: monotonic-array
# source_path: LeetCode-Solutions-master/Python/monotonic-array.py
# solution_class: Solution
# submission_id: df9082901bc0b1688275f0d2fd9584a918662282
# seed: 2551798324

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, dec = False, False
        for i in xrange(len(A)-1):
            if A[i] < A[i+1]:
                inc = True
            elif A[i] > A[i+1]:
                dec = True
        return not inc or not dec