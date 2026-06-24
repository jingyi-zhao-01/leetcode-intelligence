# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: triples-with-bitwise-and-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/triples-with-bitwise-and-equal-to-zero.py
# solution_class: Solution
# submission_id: ba92ba3b91795e9846beabd18bfbb4e7d0c66098
# seed: 3481461977

# Time:  O(nlogn), n is the max of A
# Space: O(n)

import collections


# Reference: https://blog.csdn.net/john123741/article/details/76576925
# FWT solution

class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def FWT(A, v):
            B = A[:]
            d = 1
            while d < len(B):
                for i in xrange(0, len(B), d << 1):
                    for j in xrange(d):
                        B[i+j] += B[i+j+d] * v
                d <<= 1
            return B

        k = 3
        n, max_A = 1, max(A)
        while n <= max_A:
            n *= 2
        count = collections.Counter(A)
        B = [count[i] for i in xrange(n)]
        C = FWT(map(lambda x : x**k, FWT(B, 1)), -1)
        return C[0]