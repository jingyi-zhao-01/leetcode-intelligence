# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-element-in-a-sorted-array
# source_path: LeetCode-Solutions-master/Python/single-element-in-a-sorted-array.py
# solution_class: Solution
# submission_id: 46b455e7be4d79373ff2f3266ab068c92c5a2ba6
# seed: 3002716551

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) / 2
            if not (mid%2 == 0 and mid+1 < len(nums) and \
                    nums[mid] == nums[mid+1]) and \
               not (mid%2 == 1 and nums[mid] == nums[mid-1]):
                right = mid-1
            else:
                left = mid+1
        return nums[left]