# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-whose-sum-is-less-than-target
# source_path: LeetCode-Solutions-master/Python/count-pairs-whose-sum-is-less-than-target.py
# solution_class: Solution
# submission_id: b67d046290d95a44f5ec9eb213203d32cea8ce3b
# seed: 1991804015

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers

class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left]+nums[right] < target:
                result += right-left
                left += 1
            else:
                right -= 1
        return result