# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-in-rotated-sorted-array
# source_path: LeetCode-Solutions-master/Python/find-minimum-in-rotated-sorted-array.py
# solution_class: Solution2
# submission_id: 653466de165905dcf0ea8fa0e97748041d66ddc6
# seed: 3570042767

# Time:  O(logn)
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

            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]