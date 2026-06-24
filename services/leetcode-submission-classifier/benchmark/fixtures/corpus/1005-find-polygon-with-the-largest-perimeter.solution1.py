# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-polygon-with-the-largest-perimeter
# source_path: LeetCode-Solutions-master/Python/find-polygon-with-the-largest-perimeter.py
# solution_class: Solution
# submission_id: 0121b80c5528eeb5ca9cba20e70d743d4568dbd3
# seed: 841440010

# Time:  O(nlogn)
# Space: O(1)

# sort, prefix sum, greedy

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prefix = sum(nums)
        for i in reversed(xrange(2, len(nums))):
            prefix -= nums[i]
            if prefix > nums[i]:
                return prefix+nums[i]
        return -1