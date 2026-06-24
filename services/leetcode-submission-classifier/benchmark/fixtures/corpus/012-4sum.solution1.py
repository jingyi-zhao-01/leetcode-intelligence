# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 4sum
# source_path: LeetCode-Solutions-master/Python/4sum.py
# solution_class: Solution
# submission_id: 1cf16636266885956080f0109e17dc4926f9f052
# seed: 2043503918

# Time:  O(n^3)
# Space: O(1)

import collections


# Two pointer solution. (1356ms)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in xrange(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1
        return result