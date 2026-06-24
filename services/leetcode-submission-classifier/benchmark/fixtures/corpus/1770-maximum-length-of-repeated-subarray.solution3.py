# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-repeated-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-repeated-subarray.py
# solution_class: Solution3
# submission_id: 082a815b27c6eed3ec9a3d1d86a244855b806356
# seed: 1724167170

# Time:  O(m * n)
# Space: O(min(m, n))

import collections

class Solution3(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) > len(B): return self.findLength(B, A)

        def check(length):
            lookup = set(A[i:i+length] \
                       for i in xrange(len(A)-length+1))
            return any(B[j:j+length] in lookup \
                       for j in xrange(len(B)-length+1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = left + (right-left)/2
            if not check(mid):  # find the min idx such that check(idx) == false
                right = mid
            else:
                left = mid+1
        return left-1