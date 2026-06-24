# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-sum
# source_path: LeetCode-Solutions-master/Python/two-sum.py
# solution_class: Solution
# submission_id: 0b313be67d3655b588878bb5769d7ee910fad6cc
# seed: 3309909903

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            j = target - i
            tmp_nums_start_index = nums.index(i) + 1
            tmp_nums = nums[tmp_nums_start_index:]
            if j in tmp_nums:
                return [nums.index(i), tmp_nums_start_index + tmp_nums.index(j)]