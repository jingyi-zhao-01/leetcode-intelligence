# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-colors
# source_path: LeetCode-Solutions-master/Python/sort-colors.py
# solution_class: Solution
# submission_id: 68f6e9285b977c1fa48a09eb319f61a54b081fa1
# seed: 2156211781

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def triPartition(nums, target):
            i, left, right = 0, 0, len(nums)-1
            while i <= right:
                if nums[i] > target:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                else:
                    if nums[i] < target:
                        nums[left], nums[i] = nums[i], nums[left]
                        left += 1
                    i += 1

        triPartition(nums, 1)