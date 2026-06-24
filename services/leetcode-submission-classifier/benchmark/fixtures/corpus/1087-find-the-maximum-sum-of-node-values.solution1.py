# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-sum-of-node-values
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-sum-of-node-values.py
# solution_class: Solution
# submission_id: 27018b822a08effe7458037a5608f78479064f2d
# seed: 2886667489

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        result = parity = 0
        diff = float("inf")
        for x in nums:
            y = x^k
            result += max(x, y)
            parity ^= int(x < y)
            diff = min(diff, abs(x-y))
        return result-parity*diff