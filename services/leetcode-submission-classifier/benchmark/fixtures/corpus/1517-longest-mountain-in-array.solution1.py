# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-mountain-in-array
# source_path: LeetCode-Solutions-master/Python/longest-mountain-in-array.py
# solution_class: Solution
# submission_id: 315700eff53a637c1a7e3d63fdbd1f5aff917181
# seed: 981600671

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, up_len, down_len = 0, 0, 0
        for i in xrange(1, len(A)):
            if (down_len and A[i-1] < A[i]) or A[i-1] == A[i]:
                up_len, down_len = 0, 0
            up_len += A[i-1] < A[i]
            down_len += A[i-1] > A[i]
            if up_len and down_len:
                result = max(result, up_len+down_len+1)
        return result