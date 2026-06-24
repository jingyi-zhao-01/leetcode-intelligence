# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/sum-in-a-matrix.py
# solution_class: Solution
# submission_id: c6e1bc016e37c75296637185154f5893fa3359aa
# seed: 3634286513

# Time:  O(m * nlogn)
# Space: O(1)

# sort

class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for row in nums:
            row.sort()
        return sum(max(nums[r][c] for r in xrange(len(nums))) for c in xrange(len(nums[0])))