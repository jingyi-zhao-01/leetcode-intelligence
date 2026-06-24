# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-sum-of-sub-matrix-no-larger-than-k
# source_path: LeetCode-Solutions-master/Python/max-sum-of-sub-matrix-no-larger-than-k.py
# solution_class: Solution
# submission_id: 1b7b50c5f1f4980e903b36bf0b8a4199a93cbe8d
# seed: 40004901

# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))

from bisect import bisect_left, insort

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")

        for i in xrange(m):
            sums = [0] * n
            for j in xrange(i, m):
                for l in xrange(n):
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]

                # Find the max subarray no more than K.
                accu_sum_set, accu_sum = [0], 0
                for sum in sums:
                    accu_sum += sum
                    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn)
                    if it != len(accu_sum_set):
                        result = max(result, accu_sum - accu_sum_set[it])
                    insort(accu_sum_set, accu_sum)  # Time: O(n)

        return result