# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-array-into-arrays-with-max-difference
# source_path: LeetCode-Solutions-master/Python/divide-array-into-arrays-with-max-difference.py
# solution_class: Solution
# submission_id: 1eb3457f5afac9fe5258f14be2e025e86eb6c507
# seed: 2310300157

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return [nums[i:i+3] for i in xrange(0, len(nums), 3)] if all(nums[i+2]-nums[i] <= k for i in xrange(0, len(nums), 3)) else []