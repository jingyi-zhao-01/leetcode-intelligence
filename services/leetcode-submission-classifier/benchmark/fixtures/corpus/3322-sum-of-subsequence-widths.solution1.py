# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-subsequence-widths
# source_path: LeetCode-Solutions-master/Python/sum-of-subsequence-widths.py
# solution_class: Solution
# submission_id: 0d622981fcce954ea6c27a5ad260757378a0ce42
# seed: 2164749869

# Time:  O(n)
# Spce:  O(1)

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 10**9+7
        # sum(A[i] * (2^i - 2^(len(A)-1-i))), i = 0..len(A)-1
        # <=>
        # sum(((A[i] - A[len(A)-1-i]) * 2^i), i = 0..len(A)-1
        result, c = 0, 1
        A.sort()
        for i in xrange(len(A)):
            result = (result + (A[i]-A[len(A)-1-i])*c % M) % M
            c = (c<<1) % M
        return result