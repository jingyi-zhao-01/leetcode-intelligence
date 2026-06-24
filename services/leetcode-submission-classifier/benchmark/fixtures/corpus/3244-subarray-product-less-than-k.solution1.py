# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarray-product-less-than-k
# source_path: LeetCode-Solutions-master/Python/subarray-product-less-than-k.py
# solution_class: Solution
# submission_id: e5dd90f48676c6a905aedbe856d8a3ceb912e77d
# seed: 1979928609

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        result, start, prod = 0, 0, 1
        for i, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[start]
                start += 1
            result += i-start+1
        return result