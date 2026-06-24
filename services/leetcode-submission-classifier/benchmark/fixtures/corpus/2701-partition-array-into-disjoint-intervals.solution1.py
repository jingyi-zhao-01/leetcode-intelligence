# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-into-disjoint-intervals
# source_path: LeetCode-Solutions-master/Python/partition-array-into-disjoint-intervals.py
# solution_class: Solution
# submission_id: 2db027187ff63226b7aa597cf1d14e59475b9bc0
# seed: 3079523891

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = A[:]
        for i in reversed(xrange(len(A)-1)):
            B[i] = min(B[i], B[i+1])
        p_max = 0
        for i in xrange(1, len(A)):
            p_max = max(p_max, A[i-1])
            if p_max <= B[i]:
                return i