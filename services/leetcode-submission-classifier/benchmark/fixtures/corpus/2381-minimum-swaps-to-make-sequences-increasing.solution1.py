# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-make-sequences-increasing
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-make-sequences-increasing.py
# solution_class: Solution
# submission_id: ef212bba19ff2baabf2ca7eb000933a4386e8ea3
# seed: 3788970134

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp_no_swap, dp_swap = [0]*2, [1]*2
        for i in xrange(1, len(A)):
            dp_no_swap[i%2], dp_swap[i%2] = float("inf"), float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                dp_no_swap[i%2] = min(dp_no_swap[i%2], dp_no_swap[(i-1)%2])
                dp_swap[i%2] = min(dp_swap[i%2], dp_swap[(i-1)%2]+1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                dp_no_swap[i%2] = min(dp_no_swap[i%2], dp_swap[(i-1)%2])
                dp_swap[i%2] = min(dp_swap[i%2], dp_no_swap[(i-1)%2]+1)
        return min(dp_no_swap[(len(A)-1)%2], dp_swap[(len(A)-1)%2])