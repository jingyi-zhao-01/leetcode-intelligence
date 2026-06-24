# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-beauty-in-the-array
# source_path: LeetCode-Solutions-master/Python/sum-of-beauty-in-the-array.py
# solution_class: Solution
# submission_id: c867780a93d067cd045281a3bd800c0c6e4dc44b
# seed: 2221968456

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [nums[-1]]*len(nums)
        for i in reversed(xrange(2, len(nums)-1)):
            right[i] = min(right[i+1], nums[i])
        result, left = 0, nums[0]
        for i in xrange(1, len(nums)-1):
            if left < nums[i] < right[i+1]:
                result += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
            left = max(left, nums[i])
        return result