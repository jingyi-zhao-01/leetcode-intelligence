# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strength-of-a-group
# source_path: LeetCode-Solutions-master/Python/maximum-strength-of-a-group.py
# solution_class: Solution
# submission_id: 482d6a23e89e3a5a9ebc804ab18af824871631e5
# seed: 205119275

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all(x <= 0 for x in nums) and sum(x < 0 for x in nums) <= 1:
            return max(nums)
        result = reduce(lambda x, y: x*y, (x for x in nums if x))
        return result if result > 0 else result//max(x for x in nums if x < 0)