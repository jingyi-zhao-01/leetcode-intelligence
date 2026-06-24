# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference-between-two-values
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference-between-two-values.py
# solution_class: Solution
# submission_id: 74a6d40e640780a78e1e9d4f76c0a74a363bfb8a
# seed: 451611549

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF = float("inf")
        result = INF
        i = j = -1
        for k in xrange(len(nums)):
            if nums[k] == 0:
                continue
            if nums[k] == 1:
                i = k
            else:
                j = k
            if i != -1 != j:
                result = min(result, abs(i-j))
        return result if result is not INF else -1