# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-circular-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-sum-circular-subarray.py
# solution_class: Solution
# submission_id: 0023c28c6b511b058daefd0e30c2f208a05744a5
# seed: 752584465

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total, max_sum, cur_max, min_sum, cur_min = 0, -float("inf"), 0, float("inf"), 0
        for a in A:
            cur_max = max(cur_max+a, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min+a, a)
            min_sum = min(min_sum, cur_min)
            total += a
        return max(max_sum, total-min_sum) if max_sum >= 0 else max_sum