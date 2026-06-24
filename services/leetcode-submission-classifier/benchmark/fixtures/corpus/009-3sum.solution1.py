# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 3sum
# source_path: LeetCode-Solutions-master/Python/3sum.py
# solution_class: Solution
# submission_id: 4601bd19f6ec7415e19eb6136fde3e7e1c71e889
# seed: 2242896011

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in reversed(xrange(2, len(nums))):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            target = -nums[i]
            left, right = 0, i-1
            while left < right:
                if nums[left]+nums[right] < target:
                    left += 1
                elif nums[left]+nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return result