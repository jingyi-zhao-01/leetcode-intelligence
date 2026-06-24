# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-sorted-array
# source_path: LeetCode-Solutions-master/Python/merge-sorted-array.py
# solution_class: Solution
# submission_id: 870807807c4b1477cd072842825c98970efd2f67
# seed: 2866496108

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
                A[last] = B[j]
                last, j = last - 1, j - 1