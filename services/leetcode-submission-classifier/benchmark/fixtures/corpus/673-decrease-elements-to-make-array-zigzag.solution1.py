# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decrease-elements-to-make-array-zigzag
# source_path: LeetCode-Solutions-master/Python/decrease-elements-to-make-array-zigzag.py
# solution_class: Solution
# submission_id: 83c76e7295f3b9c932914220d3c4392824ff8d72
# seed: 2499702602

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0, 0]
        for i in xrange(len(nums)):
            left = nums[i-1] if i-1 >= 0 else float("inf")
            right = nums[i+1] if i+1 < len(nums) else float("inf")
            result[i%2] += max(nums[i] - min(left, right) + 1, 0)
        return min(result)