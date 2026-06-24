# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-elements-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/make-array-elements-equal-to-zero.py
# solution_class: Solution
# submission_id: e28c074851b98cee0543c3fa204652468bdbf23f
# seed: 2075948394

# Time:  O(n)
# Space: O(1)

# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)

class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        result = curr = 0
        for x in nums:
            if not x:
                result += max(2-abs(curr-(total-curr)), 0)
            else:
                curr += x
        return result