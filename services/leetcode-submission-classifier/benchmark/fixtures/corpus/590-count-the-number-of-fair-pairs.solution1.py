# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-fair-pairs
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-fair-pairs.py
# solution_class: Solution
# submission_id: 462ea8ac5729a19e7f4e6961093cb2c0fb902e1c
# seed: 370786769

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def count(x):
            cnt = 0
            left, right = 0, len(nums)-1
            while left < right:
                if nums[left]+nums[right] <= x:
                    cnt += right-left
                    left += 1
                else:
                    right -= 1
            return cnt
        
        nums.sort()
        return count(upper)-count(lower-1)