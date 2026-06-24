# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-parity
# source_path: LeetCode-Solutions-master/Python/sort-array-by-parity.py
# solution_class: Solution
# submission_id: 7cf0e1b373bde15064b643ee383282c1e9ceeb93
# seed: 3933835860

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in xrange(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A