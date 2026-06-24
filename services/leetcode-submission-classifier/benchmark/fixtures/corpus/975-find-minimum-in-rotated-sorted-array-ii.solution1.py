# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-in-rotated-sorted-array-ii
# source_path: LeetCode-Solutions-master/Python/find-minimum-in-rotated-sorted-array-ii.py
# solution_class: Solution
# submission_id: 0c1690b58b656f9b249849f1898d7207486453e8
# seed: 4049487496

# Time:  O(logn) ~ O(n)
# Space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]