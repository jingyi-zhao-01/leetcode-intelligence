# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-in-rotated-sorted-array
# source_path: LeetCode-Solutions-master/Python/search-in-rotated-sorted-array.py
# solution_class: Solution
# submission_id: 3f14213cacca774ce03f204e697d449058e51906
# seed: 3626408991

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                return mid
            elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return -1