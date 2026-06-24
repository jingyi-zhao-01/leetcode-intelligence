# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-in-rotated-sorted-array-ii
# source_path: LeetCode-Solutions-master/Python/find-minimum-in-rotated-sorted-array-ii.py
# solution_class: Solution2
# submission_id: 49fce425bd633eb4e36f3ee9eb3129e66b4c0c0c
# seed: 1912900338

# Time:  O(logn) ~ O(n)
# Space: O(1)

class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:
            mid = left + (right - left) / 2

            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]