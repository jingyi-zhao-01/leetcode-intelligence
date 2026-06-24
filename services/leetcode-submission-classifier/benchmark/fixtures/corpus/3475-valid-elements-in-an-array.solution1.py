# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-elements-in-an-array
# source_path: LeetCode-Solutions-master/Python/valid-elements-in-an-array.py
# solution_class: Solution
# submission_id: 46c5ce0e787c5fb1d8246ca52cffe104eaef29f8
# seed: 228889398

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = [True]*len(nums)
        mx = 0
        for i in reversed(xrange(len(nums))):
            right[i] = mx < nums[i]
            mx = max(mx, nums[i])
        result = []
        mx = 0
        for i in xrange(len(nums)):
            left = mx < nums[i]
            mx = max(mx, nums[i])
            if left or right[i]:
                result.append(nums[i])
        return result