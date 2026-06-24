# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-element-in-a-sorted-matrix
# source_path: LeetCode-Solutions-master/Python/kth-smallest-element-in-a-sorted-matrix.py
# solution_class: Solution
# submission_id: 08fc1755d19c9dbd05a38cff2ed2ec4c97c9ebd2
# seed: 2862665800

# Time:  O(k * log(min(n, m, k))), with n x m matrix
# Space: O(min(n, m, k))

from heapq import heappush, heappop

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        kth_smallest = 0
        min_heap = []

        def push(i, j):
            if len(matrix) > len(matrix[0]):
                if i < len(matrix[0]) and j < len(matrix):
                    heappush(min_heap, [matrix[j][i], i, j])
            else:
                if i < len(matrix) and j < len(matrix[0]):
                    heappush(min_heap, [matrix[i][j], i, j])

        push(0, 0)
        while min_heap and k > 0:
            kth_smallest, i, j = heappop(min_heap)
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
            k -= 1

        return kth_smallest