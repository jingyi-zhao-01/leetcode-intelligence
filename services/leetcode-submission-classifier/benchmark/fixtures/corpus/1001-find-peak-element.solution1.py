# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-peak-element
# source_path: LeetCode-Solutions-master/Python/find-peak-element.py
# solution_class: Solution
# submission_id: 2b02ed99ee278419b1e8b485bf04d5baed9563ae
# seed: 623388867

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left