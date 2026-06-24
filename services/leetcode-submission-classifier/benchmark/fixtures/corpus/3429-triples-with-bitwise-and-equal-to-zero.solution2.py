# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: triples-with-bitwise-and-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/triples-with-bitwise-and-equal-to-zero.py
# solution_class: Solution2
# submission_id: d22444f7b1e9745f0977edfd89b4b7b7f8fe8a3e
# seed: 670700357

# Time:  O(nlogn), n is the max of A
# Space: O(n)

import collections


# Reference: https://blog.csdn.net/john123741/article/details/76576925
# FWT solution

class Solution2(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in xrange(len(A)):
            for j in xrange(len(A)):
                count[A[i]&A[j]] += 1
        result = 0
        for k in xrange(len(A)):
            for v in count:
                if A[k]&v == 0:
                    result += count[v]
        return result