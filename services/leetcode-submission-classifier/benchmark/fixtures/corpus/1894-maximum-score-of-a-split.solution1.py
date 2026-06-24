# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-of-a-split
# source_path: LeetCode-Solutions-master/Python/maximum-score-of-a-split.py
# solution_class: Solution
# submission_id: 3bfb57db87002b5e28b3b3446c384730b0a78e09
# seed: 621735242

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, prefix = float("-inf"), sum(nums)
        suffix = float("inf")
        for i in reversed(xrange(len(nums)-1)):
            prefix -= nums[i+1]
            suffix = min(suffix, nums[i+1])
            result = max(result, prefix-suffix)
        return result