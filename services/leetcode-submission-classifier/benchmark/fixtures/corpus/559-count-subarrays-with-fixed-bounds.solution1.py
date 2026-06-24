# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-with-fixed-bounds
# source_path: LeetCode-Solutions-master/Python/count-subarrays-with-fixed-bounds.py
# solution_class: Solution
# submission_id: 45eceaba7aa3fc0ef8d3dd82415e277076fa8ed3
# seed: 62090953

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        result = left = 0
        right = [-1]*2
        for i, x in enumerate(nums):
            if not (minK <= x <= maxK):
                left = i+1
                continue
            if x == minK:
                right[0] = i
            if x == maxK:
                right[1] = i
            result += max(min(right)-left+1, 0)
        return result