# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: neither-minimum-nor-maximum
# source_path: LeetCode-Solutions-master/Python/neither-minimum-nor-maximum.py
# solution_class: Solution2
# submission_id: b953dd63500a27c0c17e0b785d3c31e680731cdd
# seed: 1006780248

# Time:  O(n)
# Space: O(1)

# one pass, array

class Solution2(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx, mn = max(nums), min(nums)
        return next((x for x in nums if x not in (mx, mn)), -1)