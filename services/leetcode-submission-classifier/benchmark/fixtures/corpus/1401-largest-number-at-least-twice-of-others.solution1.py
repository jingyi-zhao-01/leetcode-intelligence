# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-number-at-least-twice-of-others
# source_path: LeetCode-Solutions-master/Python/largest-number-at-least-twice-of-others.py
# solution_class: Solution
# submission_id: 37c04283cfb300ad7f20b84774f45f6a775e9471
# seed: 778231094

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1