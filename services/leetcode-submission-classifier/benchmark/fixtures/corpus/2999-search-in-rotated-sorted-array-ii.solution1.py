# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-in-rotated-sorted-array-ii
# source_path: LeetCode-Solutions-master/Python/search-in-rotated-sorted-array-ii.py
# solution_class: Solution
# submission_id: 1109dc6b1b52626b7c011ff972a38322b6f74438
# seed: 3040531728

# Time:  O(logn) ~ O(n)
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
                return True
            elif nums[mid] == nums[left]:
                left += 1
            elif (nums[mid] > nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return False