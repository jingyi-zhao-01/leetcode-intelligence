# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-make-all-array-elements-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-make-all-array-elements-equal-to-zero.py
# solution_class: Solution
# submission_id: 59bdfaaeb0b46c7f06be37281c21e1b6a612d337
# seed: 3736536325

# Time:  O(n)
# Space: O(1)

# greedy, sliding window

class Solution(object):
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        curr = 0
        for i, x in enumerate(nums):
            if x-curr < 0:
                return False
            nums[i] -= curr
            curr += nums[i]
            if i-(k-1) >= 0:
                curr -= nums[i-(k-1)]
        return curr == 0