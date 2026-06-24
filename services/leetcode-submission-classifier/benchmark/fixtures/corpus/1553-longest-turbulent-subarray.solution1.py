# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-turbulent-subarray
# source_path: LeetCode-Solutions-master/Python/longest-turbulent-subarray.py
# solution_class: Solution
# submission_id: 9e8db6372b2554e6246cb80f63f8bb5a0e2d23cc
# seed: 3586355056

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 1
        start = 0
        for i in xrange(1, len(A)):
            if i == len(A)-1 or \
               cmp(A[i-1], A[i]) * cmp(A[i], A[i+1]) != -1:
                result = max(result, i-start+1)
                start = i
        return result