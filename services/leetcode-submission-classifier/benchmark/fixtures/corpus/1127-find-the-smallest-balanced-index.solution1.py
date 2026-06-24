# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-smallest-balanced-index
# source_path: LeetCode-Solutions-master/Python/find-the-smallest-balanced-index.py
# solution_class: Solution
# submission_id: ec1622a0cb6d2e38d90db15c9881b027538c2b3d
# seed: 3510886961

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = sum(nums), 1
        for i in reversed(xrange(len(nums))):
            left -= nums[i]
            if left < right:
                break
            if left == right:
                return i
            right *= nums[i]
        return -1