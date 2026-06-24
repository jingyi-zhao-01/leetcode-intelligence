# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-elements-with-strictly-smaller-and-greater-elements
# source_path: LeetCode-Solutions-master/Python/count-elements-with-strictly-smaller-and-greater-elements.py
# solution_class: Solution
# submission_id: ca535b3790f033fae12f9580e5af944bcb046bc7
# seed: 3669678616

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        return sum(mn < x < mx for x in nums)