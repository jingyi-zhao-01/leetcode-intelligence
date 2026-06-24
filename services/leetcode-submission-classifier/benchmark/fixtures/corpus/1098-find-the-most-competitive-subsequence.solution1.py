# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-most-competitive-subsequence
# source_path: LeetCode-Solutions-master/Python/find-the-most-competitive-subsequence.py
# solution_class: Solution
# submission_id: f6db8ef1aebcc70d2cd4e9e7f0b69d03ad35ac0e
# seed: 4056799258

# Time:  O(n)
# Space: O(k)

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stk = []
        for i, x in enumerate(nums):
            while stk and stk[-1] > x and len(stk)+(len(nums)-i) > k:
                stk.pop()
            if len(stk) < k:
                stk.append(x)
        return stk