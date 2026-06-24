# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-index-with-equal-value
# source_path: LeetCode-Solutions-master/Python/smallest-index-with-equal-value.py
# solution_class: Solution
# submission_id: e14a50e0db61b020c4ce642c4f4bfc9f3c3796f3
# seed: 4078603744

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return next((i for i, x in enumerate(nums) if i%10 == x), -1)