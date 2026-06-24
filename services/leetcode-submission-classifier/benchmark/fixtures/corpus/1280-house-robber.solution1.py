# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber
# source_path: LeetCode-Solutions-master/Python/house-robber.py
# solution_class: Solution
# submission_id: 2dfc5cfdc5daeda9a4ae26ba89f76cf3d0efa0bb
# seed: 135288475

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now