# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 132-pattern
# source_path: LeetCode-Solutions-master/Python/132-pattern.py
# solution_class: Solution
# submission_id: 922fc04e9ff81b109070c1cc9ca1bc2ab15957d5
# seed: 546784246

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ak = float("-inf")
        stk = []
        for i in reversed(xrange(len(nums))):
            if nums[i] < ak:
                return True
            while stk and stk[-1] < nums[i]:
                ak = stk.pop()
            stk.append(nums[i])
        return False