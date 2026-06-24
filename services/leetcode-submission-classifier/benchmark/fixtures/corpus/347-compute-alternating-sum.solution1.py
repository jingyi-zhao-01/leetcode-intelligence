# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compute-alternating-sum
# source_path: LeetCode-Solutions-master/Python/compute-alternating-sum.py
# solution_class: Solution
# submission_id: 5aabe4ff0afca6f9075ec3166291b25102243a90
# seed: 1712704350

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums[i] for i in xrange(0, len(nums), 2))-sum(nums[i] for i in xrange(1, len(nums), 2))