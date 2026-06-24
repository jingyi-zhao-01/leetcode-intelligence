# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-and-earn
# source_path: LeetCode-Solutions-master/Python/delete-and-earn.py
# solution_class: Solution
# submission_id: c08a60b8e3cba18aae8c7e66cc044395e202e784
# seed: 3291677340

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = [0] * 10001
        for num in nums:
            vals[num] += num
        val_i, val_i_1 = vals[0], 0
        for i in xrange(1, len(vals)):
            val_i_1, val_i_2 = val_i, val_i_1
            val_i = max(vals[i] + val_i_2, val_i_1)
        return val_i