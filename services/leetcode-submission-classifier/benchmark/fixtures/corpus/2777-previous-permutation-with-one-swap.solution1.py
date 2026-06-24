# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: previous-permutation-with-one-swap
# source_path: LeetCode-Solutions-master/Python/previous-permutation-with-one-swap.py
# solution_class: Solution
# submission_id: b5035ee7d3386fbf00630d730dbac92ff65edad7
# seed: 3380545928

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for left in reversed(xrange(len(A)-1)):
            if A[left] > A[left+1]:
                break
        else:
            return A
        right = len(A)-1
        while A[left] <= A[right]:
            right -= 1
        while A[right-1] == A[right]:
            right -= 1
        A[left], A[right] = A[right], A[left]
        return A