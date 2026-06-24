# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-elements-in-an-array
# source_path: LeetCode-Solutions-master/Python/valid-elements-in-an-array.py
# solution_class: Solution2
# submission_id: bbdce5f159dd1f3bfc2e1bf5c0156076cac46005
# seed: 3993659682

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution2(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [True]*len(nums)
        mx = 0
        for i in xrange(len(nums)):
            left[i] = mx < nums[i]
            mx = max(mx, nums[i])
        right = [True]*len(nums)
        mx = 0
        for i in reversed(xrange(len(nums))):
            right[i] = mx < nums[i]
            mx = max(mx, nums[i])
        return [nums[i] for i in xrange(len(nums)) if left[i] or right[i]]