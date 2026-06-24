# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-sum-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-sum-divisible-by-k.py
# solution_class: Solution
# submission_id: 7533a9a6d4d147de6392707dfeef4aa2e19a0024
# seed: 1831733090

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums)%k