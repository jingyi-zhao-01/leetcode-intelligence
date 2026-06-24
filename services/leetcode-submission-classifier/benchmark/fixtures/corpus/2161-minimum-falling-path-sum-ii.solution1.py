# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-falling-path-sum-ii
# source_path: LeetCode-Solutions-master/Python/minimum-falling-path-sum-ii.py
# solution_class: Solution
# submission_id: 9888c9867183a42a931b9e53af4ec34a753fb0aa
# seed: 195989702

# Time:  O(m * n)
# Space: O(1)

import heapq

class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(arr)):
            smallest_two = heapq.nsmallest(2, arr[i-1])
            for j in xrange(len(arr[0])):
                arr[i][j] += smallest_two[1] if arr[i-1][j] == smallest_two[0] else smallest_two[0]
        return min(arr[-1])