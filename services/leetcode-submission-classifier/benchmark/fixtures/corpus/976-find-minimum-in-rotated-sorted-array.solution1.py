# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-in-rotated-sorted-array
# source_path: LeetCode-Solutions-master/Python/find-minimum-in-rotated-sorted-array.py
# solution_class: Solution
# submission_id: 70e34f451b38ae88c1f8061b30236b45f8834459
# seed: 3691294712

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]