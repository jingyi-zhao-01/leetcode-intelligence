# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-values-equal-to-k
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-values-equal-to-k.py
# solution_class: Solution
# submission_id: 9f9b47ca8a8729586d545b31647223b17f5b2e0e
# seed: 2412877225

# Time:  O(n)
# Space: O(n)

# hash table, constructive algorithms

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mn = min(nums)
        return len(set(nums))-int(mn == k) if mn >= k else -1