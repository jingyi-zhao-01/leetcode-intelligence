# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 4sum-ii
# source_path: LeetCode-Solutions-master/Python/4sum-ii.py
# solution_class: Solution
# submission_id: 3b988b761982fee527848344db2fc482acae9442
# seed: 1455470386

# Time:  O(n^2)
# Space: O(n^2)

import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        return sum(A_B_sum[-c-d] for c in C for d in D)